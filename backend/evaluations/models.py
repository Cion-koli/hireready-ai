from django.db import models
from interviews.models import Interview, InterviewAnswer


class AnswerEvaluation(models.Model):
    """
    Detailed evaluation for each candidate answer.
    Supports both HR criteria and Technical criteria.
    """
    answer = models.OneToOneField(InterviewAnswer, on_delete=models.CASCADE, related_name='evaluation')
    is_technical = models.BooleanField(default=False)
    
    # HR Criterion scores (0 to 100)
    relevance_score = models.FloatField(null=True, blank=True, help_text="HR Weight: 30%")
    clarity_score = models.FloatField(null=True, blank=True, help_text="HR Weight: 25% | Tech Weight: 10%")
    examples_score = models.FloatField(null=True, blank=True, help_text="HR Weight: 25%")
    communication_score = models.FloatField(null=True, blank=True, help_text="HR Weight: 20%")

    # Technical Criterion scores (0 to 100)
    technical_accuracy_score = models.FloatField(null=True, blank=True, help_text="Tech Weight: 35%")
    technical_depth_score = models.FloatField(null=True, blank=True, help_text="Tech Weight: 30%")
    problem_solving_score = models.FloatField(null=True, blank=True, help_text="Tech Weight: 25%")
    
    overall_score = models.FloatField(default=0.0)
    
    # Qualitative feedback
    what_went_well = models.TextField(help_text="Strengths identified in this response")
    what_could_improve = models.TextField(help_text="Key areas for enhancement")
    improvement_suggestions = models.TextField(help_text="Actionable advice (e.g. STAR method or code tips)")
    suggested_answer_structure = models.TextField(help_text="Sample model response, code snippet, or structure")
    score_explanation = models.TextField(help_text="Justification of the score")

    # Technical specific details
    correct_points = models.TextField(blank=True, default='')
    missing_points = models.TextField(blank=True, default='')
    correct_answer_explanation = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_weighted_overall(self):
        if self.is_technical:
            acc = self.technical_accuracy_score or 0.0
            depth = self.technical_depth_score or 0.0
            ps = self.problem_solving_score or 0.0
            cla = self.clarity_score or 0.0
            return round((acc * 0.35) + (depth * 0.30) + (ps * 0.25) + (cla * 0.10), 1)
        else:
            rel = self.relevance_score or 0.0
            cla = self.clarity_score or 0.0
            ex = self.examples_score or 0.0
            com = self.communication_score or 0.0
            return round((rel * 0.30) + (cla * 0.25) + (ex * 0.25) + (com * 0.20), 1)

    def save(self, *args, **kwargs):
        if not self.overall_score:
            self.overall_score = self.calculate_weighted_overall()
        super().save(*args, **kwargs)

    def __str__(self):
        q_type = "Tech" if self.is_technical else "HR"
        return f"Eval for Q{self.answer.question.question_order} [{q_type}] (Score: {self.overall_score}%)"


class InterviewReport(models.Model):
    """
    Overall synthesized interview report for a completed or concluded interview session.
    Distinguishes HR, Technical, and Combined scores and feedback.
    """
    interview = models.OneToOneField(Interview, on_delete=models.CASCADE, related_name='report')
    interview_type = models.CharField(max_length=20, default='hr')
    
    overall_practice_score = models.FloatField(null=True, blank=True)
    hr_score = models.FloatField(null=True, blank=True)
    technical_score = models.FloatField(null=True, blank=True)
    
    # Aggregated criterion scores
    avg_relevance_score = models.FloatField(default=0.0)
    avg_clarity_score = models.FloatField(default=0.0)
    avg_examples_score = models.FloatField(default=0.0)
    avg_communication_score = models.FloatField(default=0.0)

    avg_technical_accuracy = models.FloatField(default=0.0)
    avg_technical_depth = models.FloatField(default=0.0)
    avg_problem_solving = models.FloatField(default=0.0)
    
    is_complete = models.BooleanField(default=True)
    total_questions_answered = models.PositiveIntegerField(default=0)
    
    summary = models.TextField()
    strengths = models.JSONField(default=list, help_text="General strengths observed")
    areas_for_improvement = models.JSONField(default=list, help_text="General improvement areas")

    # Separated section feedback for Combined interviews
    hr_strengths = models.JSONField(default=list, blank=True)
    hr_areas_for_improvement = models.JSONField(default=list, blank=True)
    technical_strengths = models.JSONField(default=list, blank=True)
    technical_areas_for_improvement = models.JSONField(default=list, blank=True)

    recommendations = models.JSONField(default=list, help_text="Personalized action steps")
    recommended_topics = models.JSONField(default=list, help_text="Recommended topics to practice next")
    sample_improved_answer = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Complete" if self.is_complete else "Partial"
        return f"Report: {self.interview.custom_job_role} ({self.interview_type}, {status}) - {self.overall_practice_score}%"
