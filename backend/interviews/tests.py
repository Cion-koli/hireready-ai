from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from interviews.models import Interview, InterviewQuestion, InterviewAnswer, QuestionBank
from interviews.question_banks import (
    validate_question_banks,
    ROLE_QUESTION_BANKS,
    SOFTWARE_ENGINEER_TECH_BANKS,
    ALL_PREDEFINED_QUESTIONS
)
from ai_services.validators import is_valid_hr_question, sanitize_or_replace_question, is_valid_technical_question
from evaluations.views import generate_report_for_interview


from unittest.mock import patch

class InterviewWorkflowAndGuardrailTests(TestCase):
    def setUp(self):
        self.gemini_patcher = patch('ai_services.interview_service.get_gemini_client', return_value=None)
        self.gemini_patcher.start()

        self.user1 = User.objects.create_user(username='user1', email='u1@example.com', password='password123')
        self.user2 = User.objects.create_user(username='user2', email='u2@example.com', password='password123')

        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)

        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)

    def tearDown(self):
        self.gemini_patcher.stop()

    def test_hr_guardrail_validator(self):
        """Technical questions must be rejected; HR questions must pass."""
        tech_questions = [
            "Write a python function to reverse a linked list.",
            "Write a python script to parse JSON.",
            "Explain the difference between let and var in JavaScript.",
            "Write a SQL query using SELECT * FROM employees JOIN departments.",
            "What is the time complexity and Big O of quicksort?",
            "Solve the following equation using math formulas.",
            "Write a regex pattern to validate email addresses."
        ]
        for tq in tech_questions:
            self.assertFalse(
                is_valid_hr_question(tq),
                f"Technical question should have failed HR guardrail: {tq}"
            )

        hr_questions = [
            "Tell me about a time you had to deal with a tight project deadline.",
            "How do you handle constructive feedback from a senior manager?",
            "Can you describe a situation where you resolved a conflict with a team member?",
            "Why are you interested in working as a Python Developer for our company?",
            "How do you explain technical concepts to non-technical stakeholders as a Data Analyst?"
        ]
        for hq in hr_questions:
            self.assertTrue(
                is_valid_hr_question(hq),
                f"Valid HR question should have passed: {hq}"
            )

    def test_sanitize_or_replace_question(self):
        """Disallowed technical question should be replaced with safe HR fallback."""
        bad_q = "Write a python script to parse JSON."
        clean_q, cat = sanitize_or_replace_question(bad_q, "Python Developer", 1)
        self.assertNotIn("Write a python script", clean_q)
        self.assertIn("Python Developer", clean_q)
        self.assertTrue(is_valid_hr_question(clean_q))

    def test_custom_role_interview_workflow(self):
        """User can type any custom job role and practice an HR-only interview."""
        custom_roles = ["Python Developer", "Frontend Developer", "Data Analyst", "Robotics System Architect"]

        for role in custom_roles:
            create_res = self.client1.post('/api/interviews/', {
                "interview_type": "hr",
                "custom_job_role": role,
                "experience_level": "entry",
                "difficulty": "medium",
                "interview_mode": "text",
                "question_count": 5
            }, format='json')
            self.assertEqual(create_res.status_code, status.HTTP_201_CREATED)
            interview_id = create_res.data['id']
            self.assertEqual(create_res.data['custom_job_role'], role)

            # Request first question
            next_res = self.client1.get(f'/api/interviews/{interview_id}/questions/next/')
            self.assertEqual(next_res.status_code, status.HTTP_200_OK)
            q_text = next_res.data['question']['question_text']

            # Must be valid HR question
            self.assertTrue(
                is_valid_hr_question(q_text),
                f"Generated question for {role} was not a valid HR question: {q_text}"
            )
            self.assertGreater(len(q_text), 15)

    def test_submit_answer_and_flow(self):
        """Submit answer and advance to next question."""
        interview = Interview.objects.create(
            user=self.user1,
            custom_job_role="Data Analyst",
            question_count=5,
            status="in_progress"
        )
        q = InterviewQuestion.objects.create(
            interview=interview,
            question_text="How do you present data findings to non-technical leaders?",
            question_order=1
        )

        ans_res = self.client1.post(f'/api/interviews/{interview.id}/answers/', {
            "question_id": q.id,
            "answer_text": "I prepare clear visual charts and avoid technical jargon, focusing on business ROI."
        }, format='json')
        self.assertEqual(ans_res.status_code, status.HTTP_200_OK)
        self.assertEqual(ans_res.data['answered_count'], 1)

        # Check DB persistence
        self.assertTrue(InterviewAnswer.objects.filter(question=q).exists())

    def test_question_limit_enforcement(self):
        """Interview stops when configured question limit is reached."""
        interview = Interview.objects.create(
            user=self.user1,
            custom_job_role="HR Executive",
            question_count=5,
            status="in_progress"
        )
        for i in range(1, 6):
            q = InterviewQuestion.objects.create(
                interview=interview,
                question_text=f"HR question #{i} for HR Executive?",
                question_order=i
            )
            InterviewAnswer.objects.create(
                question=q,
                answer_text=f"This is my detailed behavioral answer for question #{i}."
            )

        next_res = self.client1.get(f'/api/interviews/{interview.id}/questions/next/')
        self.assertEqual(next_res.status_code, status.HTTP_200_OK)
        self.assertTrue(next_res.data.get('is_completed'))
        self.assertEqual(next_res.data.get('answered_count'), 5)

    def test_authorization_isolation(self):
        """User 2 must not be able to view, answer, or delete User 1's interview."""
        interview1 = Interview.objects.create(
            user=self.user1,
            custom_job_role="Cloud Engineer",
            question_count=5
        )

        res = self.client2.get(f'/api/interviews/{interview1.id}/')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

        del_res = self.client2.delete(f'/api/interviews/{interview1.id}/')
        self.assertEqual(del_res.status_code, status.HTTP_404_NOT_FOUND)


class TechnicalInterviewAndQuestionBankTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Seed question bank in test database
        for q in ALL_PREDEFINED_QUESTIONS:
            QuestionBank.objects.create(
                role=q["role"],
                technology=q.get("technology", ""),
                category=q.get("category", ""),
                difficulty=q.get("difficulty", "medium"),
                question_text=q["question_text"],
                expected_answer=q.get("expected_answer", ""),
                rubric=q.get("rubric", {}),
                code_snippet=q.get("code_snippet") or "",
                follow_up_hint=q.get("follow_up_hint") or ""
            )

    def setUp(self):
        self.gemini_patcher = patch('ai_services.interview_service.get_gemini_client', return_value=None)
        self.gemini_patcher.start()

        self.user = User.objects.create_user(username='tech_user', email='tech@example.com', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        self.gemini_patcher.stop()

    def test_question_bank_minimum_counts_and_coverage(self):
        """
        Validates that:
        1. Every technical role has >= 25 questions in the bank.
        2. Software Engineer role has >= 125 total questions.
        3. Software Engineer has >= 25 questions in EACH of: Python, HTML, CSS, JavaScript, SQL.
        """
        is_valid, report = validate_question_banks()
        self.assertTrue(is_valid, f"Question bank validation failed: {report}")

        # Check in DB
        for role_name, q_list in ROLE_QUESTION_BANKS.items():
            db_count = QuestionBank.objects.filter(role=role_name).count()
            min_req = 125 if role_name == "Software Engineer" else 25
            self.assertGreaterEqual(
                db_count,
                min_req,
                f"Role {role_name} has {db_count} questions in DB, required at least {min_req}"
            )

        # Check SE 5 technologies
        for tech in ["python", "html", "css", "javascript", "sql"]:
            tech_count = QuestionBank.objects.filter(role="Software Engineer", technology=tech).count()
            self.assertGreaterEqual(
                tech_count,
                25,
                f"Software Engineer tech {tech} has {tech_count} questions in DB, required >= 25"
            )

    def test_technical_interview_workflow(self):
        """Technical interview asks role-specific technical questions only."""
        create_res = self.client.post('/api/interviews/', {
            "interview_type": "technical",
            "custom_job_role": "Python Developer",
            "experience_level": "entry",
            "difficulty": "medium",
            "interview_mode": "text",
            "question_count": 5
        }, format='json')
        self.assertEqual(create_res.status_code, status.HTTP_201_CREATED)
        interview_id = create_res.data['id']
        self.assertEqual(create_res.data['interview_type'], 'technical')

        # Request next question
        next_res = self.client.get(f'/api/interviews/{interview_id}/questions/next/')
        self.assertEqual(next_res.status_code, status.HTTP_200_OK)
        q_data = next_res.data['question']
        self.assertTrue(q_data['is_technical'])
        self.assertNotEqual(q_data['topic'], 'Behavioral')
        self.assertTrue(is_valid_technical_question(q_data['question_text']))

    def test_software_engineer_technology_filtering(self):
        """Software Engineer role respects technology filters (e.g. Python only)."""
        create_res = self.client.post('/api/interviews/', {
            "interview_type": "technical",
            "custom_job_role": "Software Engineer",
            "selected_technologies": ["python"],
            "experience_level": "experienced",
            "difficulty": "hard",
            "interview_mode": "text",
            "question_count": 5
        }, format='json')
        self.assertEqual(create_res.status_code, status.HTTP_201_CREATED)
        interview_id = create_res.data['id']

        # Fetch questions and ensure they are Python technical questions
        asked_ids = set()
        for i in range(1, 4):
            next_res = self.client.get(f'/api/interviews/{interview_id}/questions/next/')
            self.assertEqual(next_res.status_code, status.HTTP_200_OK)
            q = next_res.data['question']
            self.assertTrue(q['is_technical'])
            self.assertNotIn(q['id'], asked_ids)
            asked_ids.add(q['id'])

            # Submit answer to advance
            self.client.post(f'/api/interviews/{interview_id}/answers/', {
                "question_id": q['id'],
                "answer_text": "Generators in Python use yield and maintain state across iterations without holding everything in memory."
            }, format='json')

    def test_combined_interview_workflow(self):
        """Combined interview includes both HR and Technical questions (~30% HR, ~70% Tech)."""
        create_res = self.client.post('/api/interviews/', {
            "interview_type": "combined",
            "custom_job_role": "Backend Developer",
            "experience_level": "entry",
            "difficulty": "medium",
            "interview_mode": "text",
            "question_count": 5
        }, format='json')
        self.assertEqual(create_res.status_code, status.HTTP_201_CREATED)
        interview_id = create_res.data['id']

        # Answer all 5 questions and track types
        types_encountered = []
        for i in range(1, 6):
            next_res = self.client.get(f'/api/interviews/{interview_id}/questions/next/')
            self.assertEqual(next_res.status_code, status.HTTP_200_OK)
            q = next_res.data['question']
            types_encountered.append(q['is_technical'])

            self.client.post(f'/api/interviews/{interview_id}/answers/', {
                "question_id": q['id'],
                "answer_text": "This is a structured response answering the question with practical examples and details."
            }, format='json')

        # Verify both HR (False) and Technical (True) are present
        self.assertIn(False, types_encountered, "Combined interview must include HR questions")
        self.assertIn(True, types_encountered, "Combined interview must include Technical questions")

    def test_technical_evaluation_and_combined_report(self):
        """Evaluates technical questions with technical rubric and creates separated combined report."""
        interview = Interview.objects.create(
            user=self.user,
            interview_type="combined",
            custom_job_role="Full-Stack Developer",
            question_count=2,
            status="in_progress"
        )
        # Q1: HR question
        q1 = InterviewQuestion.objects.create(
            interview=interview,
            question_text="Tell me about a time you handled a difficult conflict with a project stakeholder.",
            question_order=1,
            is_technical=False
        )
        InterviewAnswer.objects.create(
            question=q1,
            answer_text="When requirements conflicted, I held a cross-functional alignment meeting and used the STAR framework to resolve priorities."
        )

        # Q2: Technical question
        q2 = InterviewQuestion.objects.create(
            interview=interview,
            question_text="Explain how database indexes improve SELECT query speed and why they incur an INSERT penalty.",
            question_order=2,
            is_technical=True,
            topic="Database Indexing",
            expected_answer="B-trees allow logarithmic search O(log N) for lookups but require tree updates and rebalancing on writes."
        )
        InterviewAnswer.objects.create(
            question=q2,
            answer_text="B-Tree indexes sort keys so lookups take O(log N). On INSERTs the database must write to both table and index leaf blocks."
        )

        # Generate report
        report = generate_report_for_interview(interview, is_complete=True)
        self.assertIsNotNone(report.overall_practice_score)
        self.assertIsNotNone(report.hr_score)
        self.assertIsNotNone(report.technical_score)
        self.assertEqual(report.interview_type, 'combined')

        # Check individual evaluations
        eval1 = q1.answer.evaluation
        eval2 = q2.answer.evaluation
        self.assertFalse(eval1.is_technical)
        self.assertTrue(eval2.is_technical)
        self.assertIsNotNone(eval2.technical_accuracy_score)
        self.assertIsNotNone(eval2.correct_points)
