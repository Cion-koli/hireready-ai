from rest_framework import serializers
from .models import Interview, InterviewQuestion, InterviewAnswer, QuestionBank


class InterviewAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewAnswer
        fields = ['id', 'answer_text', 'is_voice_transcribed', 'created_at']


class InterviewQuestionSerializer(serializers.ModelSerializer):
    answer = InterviewAnswerSerializer(read_only=True)

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
            'follow_up_to',
            'answer',
            'created_at'
        ]


class InterviewListSerializer(serializers.ModelSerializer):
    answered_count = serializers.IntegerField(source='answered_questions_count', read_only=True)
    report_id = serializers.SerializerMethodField()
    overall_score = serializers.SerializerMethodField()

    class Meta:
        model = Interview
        fields = [
            'id',
            'interview_type',
            'custom_job_role',
            'selected_technologies',
            'experience_level',
            'difficulty',
            'interview_mode',
            'question_count',
            'status',
            'is_demo',
            'answered_count',
            'report_id',
            'overall_score',
            'created_at',
            'started_at',
            'completed_at'
        ]

    def get_report_id(self, obj):
        return obj.report.id if hasattr(obj, 'report') else None

    def get_overall_score(self, obj):
        if hasattr(obj, 'report') and obj.report.overall_practice_score is not None:
            return obj.report.overall_practice_score
        return None


class InterviewDetailSerializer(serializers.ModelSerializer):
    questions = InterviewQuestionSerializer(many=True, read_only=True)
    answered_count = serializers.IntegerField(source='answered_questions_count', read_only=True)
    report_id = serializers.SerializerMethodField()
    overall_score = serializers.SerializerMethodField()

    class Meta:
        model = Interview
        fields = [
            'id',
            'interview_type',
            'custom_job_role',
            'selected_technologies',
            'experience_level',
            'difficulty',
            'interview_mode',
            'question_count',
            'job_description',
            'resume_text',
            'interview_focus',
            'status',
            'is_demo',
            'questions',
            'answered_count',
            'report_id',
            'overall_score',
            'created_at',
            'started_at',
            'completed_at'
        ]

    def get_report_id(self, obj):
        return obj.report.id if hasattr(obj, 'report') else None

    def get_overall_score(self, obj):
        if hasattr(obj, 'report') and obj.report.overall_practice_score is not None:
            return obj.report.overall_practice_score
        return None


class CreateInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = [
            'interview_type',
            'custom_job_role',
            'selected_technologies',
            'experience_level',
            'difficulty',
            'interview_mode',
            'question_count',
            'job_description',
            'resume_text',
            'interview_focus'
        ]

    def validate_custom_job_role(self, value):
        val = value.strip()
        if not val or len(val) < 2:
            raise serializers.ValidationError("Please provide a valid job role (at least 2 characters).")
        return val

    def validate_question_count(self, value):
        if value not in [5, 10, 15]:
            raise serializers.ValidationError("Question count must be 5, 10, or 15.")
        return value

    def validate_interview_type(self, value):
        if value not in ['hr', 'technical', 'combined']:
            raise serializers.ValidationError("Interview type must be hr, technical, or combined.")
        return value
