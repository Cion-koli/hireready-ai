from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from interviews.models import Interview, InterviewQuestion, InterviewAnswer
from evaluations.models import AnswerEvaluation, InterviewReport
from evaluations.views import generate_report_for_interview


class EvaluationAndReportTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='tester@example.com', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_weighted_scoring_calculation(self):
        """Weights must be 30% relevance, 25% clarity, 25% examples, 20% communication."""
        interview = Interview.objects.create(
            user=self.user,
            custom_job_role="Full-Stack Developer",
            question_count=5
        )
        q = InterviewQuestion.objects.create(
            interview=interview,
            question_text="Tell me about a time you handled a conflict.",
            question_order=1
        )
        ans = InterviewAnswer.objects.create(
            question=q,
            answer_text="In our team we had different opinions on release dates so we discussed them openly."
        )

        eval_obj = AnswerEvaluation(
            answer=ans,
            relevance_score=80.0,    # 80 * 0.30 = 24.0
            clarity_score=70.0,      # 70 * 0.25 = 17.5
            examples_score=60.0,     # 60 * 0.25 = 15.0
            communication_score=90.0 # 90 * 0.20 = 18.0
            # Total expected: 24.0 + 17.5 + 15.0 + 18.0 = 74.5
        )
        eval_obj.save()
        self.assertEqual(eval_obj.overall_score, 74.5)

    def test_report_generation_from_saved_answers(self):
        """Generating a report evaluates answers and creates structured feedback report."""
        interview = Interview.objects.create(
            user=self.user,
            custom_job_role="Product Designer",
            question_count=5,
            status="in_progress"
        )
        q1 = InterviewQuestion.objects.create(
            interview=interview,
            question_text="Why do you want to work as a Product Designer?",
            question_order=1
        )
        InterviewAnswer.objects.create(
            question=q1,
            answer_text="I am passionate about user research, empathy in product interfaces, and solving real user problems."
        )

        report = generate_report_for_interview(interview, is_complete=True)
        self.assertIsNotNone(report)
        self.assertEqual(report.total_questions_answered, 1)
        self.assertIsNotNone(report.overall_practice_score)
        self.assertTrue(len(report.strengths) > 0)
        self.assertTrue(len(report.areas_for_improvement) > 0)

        # Verify via API endpoint
        res = self.client.get(f'/api/reports/{report.id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['custom_job_role'], "Product Designer")
        self.assertEqual(len(res.data['qa_breakdown']), 1)
