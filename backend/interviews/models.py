from django.db import models
from django.contrib.auth.models import User


class QuestionBank(models.Model):
    """
    Permanent structured technical question bank for predefined technical roles and technologies.
    """
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    role = models.CharField(max_length=100, db_index=True)
    technology = models.CharField(max_length=50, blank=True, default='', db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='medium')
    question_text = models.TextField()
    expected_answer = models.TextField(blank=True, default='', help_text="Core points expected in candidate answer")
    rubric = models.JSONField(default=dict, blank=True, help_text="Evaluation criteria points")
    code_snippet = models.TextField(blank=True, default='', help_text="Optional starter or reference code")
    follow_up_hint = models.TextField(blank=True, default='', help_text="Suggested technical follow-up inquiry")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['role', 'technology', 'difficulty', 'id']

    def __str__(self):
        tech = f" [{self.technology}]" if self.technology else ""
        return f"{self.role}{tech} ({self.difficulty}): {self.question_text[:60]}..."


class Interview(models.Model):
    INTERVIEW_TYPE_CHOICES = [
        ('hr', 'HR Interview'),
        ('technical', 'Technical Interview'),
        ('combined', 'Combined Interview (HR + Technical)'),
    ]

    EXPERIENCE_CHOICES = [
        ('fresher', 'Fresher'),
        ('entry', 'Entry-level'),
        ('experienced', 'Experienced'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('challenging', 'Challenging'),
    ]

    MODE_CHOICES = [
        ('text', 'Text Interview'),
        ('voice', 'Voice Interview'),
    ]

    STATUS_CHOICES = [
        ('setup', 'Setup'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('ended_early', 'Ended Early'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interviews')
    interview_type = models.CharField(max_length=20, choices=INTERVIEW_TYPE_CHOICES, default='hr')
    custom_job_role = models.CharField(max_length=255, help_text="Target job role specified by candidate")
    selected_technologies = models.JSONField(
        default=list,
        blank=True,
        help_text="Selected technologies for Software Engineer role (e.g. ['python', 'html', 'css', 'javascript', 'sql'])"
    )

    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='entry')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='medium')
    interview_mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='text')
    question_count = models.PositiveIntegerField(default=5)
    
    # Optional context
    job_description = models.TextField(blank=True, default='')
    resume_text = models.TextField(blank=True, default='')
    interview_focus = models.CharField(max_length=255, blank=True, default='')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='setup')
    is_demo = models.BooleanField(default=False, help_text="True if generated via fallback/demo mode")

    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.custom_job_role} ({self.get_interview_type_display()}) - {self.status}"

    @property
    def answered_questions_count(self):
        return self.questions.filter(answer__isnull=False).count()

    @property
    def is_finished(self):
        return self.status in ['completed', 'ended_early']


class InterviewQuestion(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name='questions')
    bank_question = models.ForeignKey(
        QuestionBank,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='instances'
    )
    question_text = models.TextField()
    question_order = models.PositiveIntegerField()
    question_category = models.CharField(max_length=100, default='behavioral')
    
    is_technical = models.BooleanField(default=False)
    topic = models.CharField(max_length=100, blank=True, default='')
    difficulty = models.CharField(max_length=20, default='medium')
    expected_answer = models.TextField(blank=True, default='')
    code_snippet = models.TextField(blank=True, default='')

    is_follow_up = models.BooleanField(default=False)
    follow_up_to = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='follow_ups'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['question_order']
        unique_together = ('interview', 'question_order')

    def __str__(self):
        q_type = "Tech" if self.is_technical else "HR"
        return f"Q{self.question_order} [{q_type}] for {self.interview.custom_job_role}: {self.question_text[:50]}..."


class InterviewAnswer(models.Model):
    question = models.OneToOneField(InterviewQuestion, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.TextField()
    is_voice_transcribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Answer to Q{self.question.question_order} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
