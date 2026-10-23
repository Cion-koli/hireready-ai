from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Interview, InterviewQuestion, InterviewAnswer
from .serializers import (
    InterviewListSerializer,
    InterviewDetailSerializer,
    CreateInterviewSerializer,
    InterviewQuestionSerializer
)
from ai_services.interview_service import generate_next_interview_question
from evaluations.views import generate_report_for_interview


class InterviewListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        queryset = Interview.objects.filter(user=user)

        # Filters
        role_query = request.query_params.get('role', '').strip()
        if role_query:
            queryset = queryset.filter(custom_job_role__icontains=role_query)

        status_query = request.query_params.get('status', '').strip()
        if status_query:
            queryset = queryset.filter(status=status_query)

        type_query = request.query_params.get('type', '').strip()
        if type_query:
            queryset = queryset.filter(interview_type=type_query)

        serializer = InterviewListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateInterviewSerializer(data=request.data)
        if serializer.is_valid():
            interview = serializer.save(user=request.user)
            return Response(InterviewDetailSerializer(interview).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InterviewDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Interview, pk=pk, user=user)

    def get(self, request, pk):
        interview = self.get_object(pk, request.user)
        return Response(InterviewDetailSerializer(interview).data)

    def delete(self, request, pk):
        interview = self.get_object(pk, request.user)
        interview.delete()
        return Response({"message": "Interview session deleted successfully."}, status=status.HTTP_200_OK)


class InterviewStartResumeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk, user=request.user)
        
        if interview.status == 'completed':
            return Response(
                {"error": "This interview has already been completed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if interview.status in ['setup', 'ended_early']:
            interview.status = 'in_progress'
            if not interview.started_at:
                interview.started_at = timezone.now()
            interview.save()

        return Response(InterviewDetailSerializer(interview).data)


class NextQuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk, user=request.user)

        if interview.status == 'completed':
            return Response(
                {"error": "Interview is already completed.", "is_completed": True},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Ensure interview is marked in_progress
        if interview.status == 'setup':
            interview.status = 'in_progress'
            interview.started_at = timezone.now()
            interview.save()

        # Check for any existing unanswered question
        unanswered = interview.questions.filter(answer__isnull=True).order_by('question_order').first()
        if unanswered:
            return Response({
                "question": InterviewQuestionSerializer(unanswered).data,
                "total_questions": interview.question_count,
                "current_number": unanswered.question_order,
                "is_completed": False
            })

        # Check if question limit reached
        answered_count = interview.questions.filter(answer__isnull=False).count()
        if answered_count >= interview.question_count:
            return Response({
                "message": "All configured questions have been answered.",
                "is_completed": True,
                "total_questions": interview.question_count,
                "answered_count": answered_count
            })

        # Build previous Q&A context
        previous_qa = []
        for q in interview.questions.filter(answer__isnull=False).order_by('question_order'):
            previous_qa.append({
                "question": q.question_text,
                "answer": q.answer.answer_text,
                "is_technical": q.is_technical
            })

        # Generate or fetch new question using updated AI service
        new_q_data = generate_next_interview_question(interview, previous_qa)
        
        if new_q_data.get('is_demo'):
            interview.is_demo = True
            interview.save(update_fields=['is_demo'])

        question_order = answered_count + 1
        follow_up_to = None
        if new_q_data.get('is_follow_up') and interview.questions.exists():
            follow_up_to = interview.questions.order_by('-question_order').first()

        new_question = InterviewQuestion.objects.create(
            interview=interview,
            question_text=new_q_data['question'],
            question_order=question_order,
            question_category=new_q_data.get('category', 'technical' if new_q_data.get('is_technical') else 'behavioral'),
            is_technical=new_q_data.get('is_technical', False),
            topic=new_q_data.get('topic', ''),
            difficulty=new_q_data.get('difficulty', interview.difficulty),
            expected_answer=new_q_data.get('expected_answer', ''),
            code_snippet=new_q_data.get('code_snippet', ''),
            bank_question=new_q_data.get('bank_question'),
            is_follow_up=new_q_data.get('is_follow_up', False),
            follow_up_to=follow_up_to
        )

        return Response({
            "question": InterviewQuestionSerializer(new_question).data,
            "total_questions": interview.question_count,
            "current_number": question_order,
            "is_completed": False
        })


class SubmitAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk, user=request.user)

        if interview.status == 'completed':
            return Response(
                {"error": "Interview is already completed. Answers cannot be submitted."},
                status=status.HTTP_400_BAD_REQUEST
            )

        question_id = request.data.get('question_id')
        answer_text = request.data.get('answer_text', '').strip()
        is_voice = bool(request.data.get('is_voice_transcribed', False))

        if not question_id:
            return Response({"error": "question_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not answer_text:
            return Response({"error": "Answer text cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        question = get_object_or_404(InterviewQuestion, pk=question_id, interview=interview)

        # Check if already answered
        if hasattr(question, 'answer'):
            answer = question.answer
            answer.answer_text = answer_text
            answer.is_voice_transcribed = is_voice
            answer.save()
        else:
            answer = InterviewAnswer.objects.create(
                question=question,
                answer_text=answer_text,
                is_voice_transcribed=is_voice
            )

        answered_count = interview.questions.filter(answer__isnull=False).count()
        is_finished = (answered_count >= interview.question_count)

        return Response({
            "message": "Answer submitted successfully",
            "answered_count": answered_count,
            "total_questions": interview.question_count,
            "is_finished": is_finished
        })


class EndInterviewEarlyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk, user=request.user)

        if interview.status == 'completed':
            return Response({"message": "Interview was already completed."}, status=status.HTTP_200_OK)

        interview.status = 'ended_early'
        interview.completed_at = timezone.now()
        interview.save()

        # Generate report for questions answered so far if any
        answered_count = interview.questions.filter(answer__isnull=False).count()
        report = None
        if answered_count > 0:
            report = generate_report_for_interview(interview, is_complete=False)

        return Response({
            "message": "Interview ended early.",
            "answered_count": answered_count,
            "report_id": report.id if report else None
        })
