from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import Avg

from interviews.models import Interview, InterviewQuestion, InterviewAnswer
from .models import AnswerEvaluation, InterviewReport
from .serializers import InterviewReportSerializer
from ai_services.interview_service import (
    evaluate_candidate_answer,
    synthesize_interview_report
)


def generate_report_for_interview(interview: Interview, is_complete: bool = True) -> InterviewReport:
    """
    Evaluates all submitted answers in the interview and compiles the final report.
    Supports HR, Technical, and Combined modes.
    """
    questions = interview.questions.filter(answer__isnull=False).select_related('answer')
    qa_eval_list = []

    # 1. Evaluate any answers that lack evaluation
    for q in questions:
        answer = q.answer
        if not hasattr(answer, 'evaluation'):
            eval_data = evaluate_candidate_answer(interview, q, answer.answer_text)
            evaluation = AnswerEvaluation.objects.create(
                answer=answer,
                is_technical=eval_data.get('is_technical', q.is_technical),
                relevance_score=eval_data.get('relevance_score'),
                clarity_score=eval_data.get('clarity_score'),
                examples_score=eval_data.get('examples_score'),
                communication_score=eval_data.get('communication_score'),
                technical_accuracy_score=eval_data.get('technical_accuracy_score'),
                technical_depth_score=eval_data.get('technical_depth_score'),
                problem_solving_score=eval_data.get('problem_solving_score'),
                overall_score=eval_data.get('overall_score', 70.0),
                correct_points=eval_data.get('correct_points', []),
                missing_points=eval_data.get('missing_points', []),
                correct_answer_explanation=eval_data.get('correct_answer_explanation', ''),
                what_went_well=eval_data.get('what_went_well', ''),
                what_could_improve=eval_data.get('what_could_improve', ''),
                improvement_suggestions=eval_data.get('improvement_suggestions', ''),
                suggested_answer_structure=eval_data.get('suggested_answer_structure', ''),
                score_explanation=eval_data.get('score_explanation', '')
            )
        else:
            evaluation = answer.evaluation

        qa_eval_list.append({
            "question": q.question_text,
            "answer": answer.answer_text,
            "is_technical": evaluation.is_technical,
            "overall_score": evaluation.overall_score,
            "what_went_well": evaluation.what_went_well,
            "what_could_improve": evaluation.what_could_improve
        })

    # 2. Compute averages
    total_answered = len(questions)
    hr_evals = AnswerEvaluation.objects.filter(answer__question__interview=interview, is_technical=False)
    tech_evals = AnswerEvaluation.objects.filter(answer__question__interview=interview, is_technical=True)

    avg_rel = round(hr_evals.aggregate(Avg('relevance_score'))['relevance_score__avg'] or 0.0, 1) if hr_evals.exists() else None
    avg_cla = round(hr_evals.aggregate(Avg('clarity_score'))['clarity_score__avg'] or 0.0, 1) if hr_evals.exists() else None
    avg_ex = round(hr_evals.aggregate(Avg('examples_score'))['examples_score__avg'] or 0.0, 1) if hr_evals.exists() else None
    avg_com = round(hr_evals.aggregate(Avg('communication_score'))['communication_score__avg'] or 0.0, 1) if hr_evals.exists() else None
    hr_score = round(hr_evals.aggregate(Avg('overall_score'))['overall_score__avg'] or 0.0, 1) if hr_evals.exists() else None

    avg_tech_acc = round(tech_evals.aggregate(Avg('technical_accuracy_score'))['technical_accuracy_score__avg'] or 0.0, 1) if tech_evals.exists() else None
    avg_tech_depth = round(tech_evals.aggregate(Avg('technical_depth_score'))['technical_depth_score__avg'] or 0.0, 1) if tech_evals.exists() else None
    avg_prob_solv = round(tech_evals.aggregate(Avg('problem_solving_score'))['problem_solving_score__avg'] or 0.0, 1) if tech_evals.exists() else None
    tech_score = round(tech_evals.aggregate(Avg('overall_score'))['overall_score__avg'] or 0.0, 1) if tech_evals.exists() else None

    all_evals = AnswerEvaluation.objects.filter(answer__question__interview=interview)
    avg_overall = round(all_evals.aggregate(Avg('overall_score'))['overall_score__avg'] or 0.0, 1) if all_evals.exists() else None

    # 3. Synthesize overall report narrative
    report_data = synthesize_interview_report(interview, qa_eval_list)

    # 4. Save or update report
    report, _ = InterviewReport.objects.update_or_create(
        interview=interview,
        defaults={
            "interview_type": interview.interview_type,
            "overall_practice_score": avg_overall,
            "hr_score": hr_score if hr_score is not None else report_data.get('hr_score'),
            "technical_score": tech_score if tech_score is not None else report_data.get('technical_score'),
            "avg_relevance_score": avg_rel,
            "avg_clarity_score": avg_cla,
            "avg_examples_score": avg_ex,
            "avg_communication_score": avg_com,
            "avg_technical_accuracy": avg_tech_acc,
            "avg_technical_depth": avg_tech_depth,
            "avg_problem_solving": avg_prob_solv,
            "is_complete": is_complete,
            "total_questions_answered": total_answered,
            "summary": report_data.get('summary', 'Interview evaluation summary.'),
            "strengths": report_data.get('strengths', []),
            "areas_for_improvement": report_data.get('areas_for_improvement', []),
            "hr_strengths": report_data.get('hr_strengths', []),
            "hr_areas_for_improvement": report_data.get('hr_areas_for_improvement', []),
            "technical_strengths": report_data.get('technical_strengths', []),
            "technical_areas_for_improvement": report_data.get('technical_areas_for_improvement', []),
            "recommendations": report_data.get('recommendations', []),
            "recommended_topics": report_data.get('recommended_topics', []),
            "sample_improved_answer": report_data.get('sample_improved_answer', '')
        }
    )

    if is_complete:
        interview.status = 'completed'
    if not interview.completed_at:
        interview.completed_at = timezone.now()
    interview.save()

    return report


class CompleteInterviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk, user=request.user)
        report = generate_report_for_interview(interview, is_complete=True)
        return Response(InterviewReportSerializer(report).data)


class InterviewReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # Can be fetched by report_id or interview_id
        try:
            report = InterviewReport.objects.get(pk=pk, interview__user=request.user)
        except InterviewReport.DoesNotExist:
            report = get_object_or_404(InterviewReport, interview_id=pk, interview__user=request.user)

        return Response(InterviewReportSerializer(report).data)


class UserReportsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reports = InterviewReport.objects.filter(interview__user=request.user).order_by('-created_at')
        return Response(InterviewReportSerializer(reports, many=True).data)


class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        interviews = Interview.objects.filter(user=user)
        reports = InterviewReport.objects.filter(interview__user=user)

        total_interviews = interviews.count()
        completed_interviews = interviews.filter(status='completed').count()

        valid_reports = reports.exclude(overall_practice_score__isnull=True)
        avg_score = valid_reports.aggregate(Avg('overall_practice_score'))['overall_practice_score__avg']
        avg_score = round(avg_score, 1) if avg_score else 0.0

        # Score trend over time (last 8 sessions)
        score_trend = []
        for rep in valid_reports.order_by('created_at')[:8]:
            score_trend.append({
                "date": rep.created_at.strftime("%b %d"),
                "role": rep.interview.custom_job_role,
                "score": rep.overall_practice_score
            })

        # Recent sessions
        from interviews.serializers import InterviewListSerializer
        recent_sessions = InterviewListSerializer(interviews.order_by('-created_at')[:5], many=True).data

        return Response({
            "total_interviews": total_interviews,
            "completed_interviews": completed_interviews,
            "average_score": avg_score,
            "recent_sessions": recent_sessions,
            "score_trend": score_trend
        })
