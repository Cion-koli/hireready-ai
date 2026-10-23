from rest_framework import serializers
from .models import AnswerEvaluation, InterviewReport
from interviews.models import InterviewQuestion, InterviewAnswer


class AnswerEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerEvaluation
        fields = [
            'id',
            'is_technical',
            'relevance_score',
            'clarity_score',
            'examples_score',
            'communication_score',
            'technical_accuracy_score',
            'technical_depth_score',
            'problem_solving_score',
            'overall_score',
            'correct_points',
            'missing_points',
            'correct_answer_explanation',
            'what_went_well',
            'what_could_improve',
            'improvement_suggestions',
            'suggested_answer_structure',
            'score_explanation',
            'created_at'
        ]


class QAEvaluationItemSerializer(serializers.ModelSerializer):
    answer_text = serializers.CharField(source='answer.answer_text', read_only=True)
    is_voice = serializers.BooleanField(source='answer.is_voice_transcribed', read_only=True)
    evaluation = serializers.SerializerMethodField()

    class Meta:
        model = InterviewQuestion
        fields = [
            'id',
            'question_order',
            'question_text',
            'question_category',
            'is_technical',
            'topic',
            'difficulty',
            'expected_answer',
            'code_snippet',
            'is_follow_up',
            'answer_text',
            'is_voice',
            'evaluation'
        ]

    def get_evaluation(self, obj):
        if hasattr(obj, 'answer') and hasattr(obj.answer, 'evaluation'):
            return AnswerEvaluationSerializer(obj.answer.evaluation).data
        return None


class InterviewReportSerializer(serializers.ModelSerializer):
    interview_type = serializers.CharField(source='interview.interview_type', read_only=True)
    custom_job_role = serializers.CharField(source='interview.custom_job_role', read_only=True)
    selected_technologies = serializers.ListField(source='interview.selected_technologies', read_only=True)
    experience_level = serializers.CharField(source='interview.experience_level', read_only=True)
    difficulty = serializers.CharField(source='interview.difficulty', read_only=True)
    interview_mode = serializers.CharField(source='interview.interview_mode', read_only=True)
    total_configured_questions = serializers.IntegerField(source='interview.question_count', read_only=True)
    is_demo = serializers.BooleanField(source='interview.is_demo', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    qa_breakdown = serializers.SerializerMethodField()

    class Meta:
        model = InterviewReport
        fields = [
            'id',
            'interview_id',
            'interview_type',
            'custom_job_role',
            'selected_technologies',
            'experience_level',
            'difficulty',
            'interview_mode',
            'total_configured_questions',
            'total_questions_answered',
            'overall_practice_score',
            'hr_score',
            'technical_score',
            'avg_relevance_score',
            'avg_clarity_score',
            'avg_examples_score',
            'avg_communication_score',
            'avg_technical_accuracy',
            'avg_technical_depth',
            'avg_problem_solving',
            'is_complete',
            'is_demo',
            'summary',
            'strengths',
            'areas_for_improvement',
            'hr_strengths',
            'hr_areas_for_improvement',
            'technical_strengths',
            'technical_areas_for_improvement',
            'recommendations',
            'recommended_topics',
            'sample_improved_answer',
            'qa_breakdown',
            'created_at'
        ]

    def get_qa_breakdown(self, obj):
        questions = obj.interview.questions.filter(answer__isnull=False).select_related('answer')
        return QAEvaluationItemSerializer(questions, many=True).data
