"""
Main AI Interview Service for HireReady AI.
Handles question retrieval from QuestionBank or dynamic generation via Gemini,
answer evaluation with HR or Technical rubrics, and comprehensive report synthesis.
"""

import json
import logging
import random
from django.conf import settings
from .prompts import (
    HR_SYSTEM_INSTRUCTION,
    TECHNICAL_SYSTEM_INSTRUCTION,
    COMBINED_SYSTEM_INSTRUCTION,
    build_question_prompt,
    build_technical_question_prompt,
    build_evaluation_prompt,
    build_technical_evaluation_prompt,
    build_report_prompt
)
from .validators import (
    sanitize_or_replace_question,
    is_valid_hr_question,
    is_valid_technical_question
)
from .mock_engine import (
    generate_mock_question,
    evaluate_mock_answer,
    evaluate_mock_technical_answer,
    generate_mock_report
)

logger = logging.getLogger(__name__)


def get_gemini_client():
    """
    Initializes and returns Google GenAI client if GEMINI_API_KEY is configured.
    Returns None if key is absent.
    """
    api_key = getattr(settings, 'GEMINI_API_KEY', '').strip()
    if not api_key:
        return None
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except Exception as e:
        logger.warning(f"Could not initialize Google GenAI SDK client: {e}")
        return None


def is_combined_stage_hr(question_index: int, total_questions: int) -> bool:
    """
    Calculates whether the given question in a combined interview is HR (~30%) or Technical (~70%).
    Ensures sensible distribution: e.g. for 5 questions (Q1 HR, Q4 HR, Q2,3,5 Tech).
    """
    if total_questions <= 2:
        return question_index == 1

    hr_target = max(1, round(total_questions * 0.30))
    if hr_target == 1:
        return question_index == 1
    elif hr_target == 2:
        midpoint = (total_questions // 2) + 1
        return question_index in (1, midpoint)
    else:
        # Distribute hr_target indices across the interview
        step = total_questions / hr_target
        hr_indices = set()
        for i in range(hr_target):
            idx = min(total_questions, max(1, int(round(1 + i * step))))
            hr_indices.add(idx)
        return question_index in hr_indices


def fetch_bank_question(interview, exclude_question_ids: list = None) -> dict:
    """
    Fetches a non-repeating technical question from the stored QuestionBank.
    Supports Software Engineer role filtering and round-robin across selected technologies.
    """
    from interviews.models import QuestionBank

    exclude_question_ids = exclude_question_ids or []
    role = interview.custom_job_role.strip()
    interview_type = interview.interview_type
    selected_techs = interview.selected_technologies or []

    qs = QuestionBank.objects.filter(role__iexact=role).exclude(id__in=exclude_question_ids)

    # For Software Engineer role: filter by selected_technologies if provided
    if role.lower() == "software engineer" and selected_techs:
        # If user picked specific technologies (e.g. ['python', 'sql'])
        # Find which technology among selected_techs has been asked least in this interview so far
        tech_counts = {t.lower(): 0 for t in selected_techs}
        already_asked_techs = interview.questions.filter(
            bank_question__isnull=False
        ).values_list('bank_question__technology', flat=True)

        for t in already_asked_techs:
            if t and t.lower() in tech_counts:
                tech_counts[t.lower()] += 1

        # Pick least asked technology among the selected ones
        least_asked_tech = min(tech_counts, key=tech_counts.get)
        tech_qs = qs.filter(technology__iexact=least_asked_tech)
        if tech_qs.exists():
            qs = tech_qs
        else:
            qs = qs.filter(technology__in=[t.lower() for t in selected_techs])

    # Filter by difficulty preference if available, but fallback gracefully
    diff = interview.difficulty.lower()
    diff_target = 'medium' if diff == 'experienced' else ('easy' if diff == 'fresher' else 'medium')
    if diff in ['easy', 'medium', 'hard']:
        diff_target = diff

    pref_qs = qs.filter(difficulty=diff_target)
    if pref_qs.exists():
        bank_q = pref_qs.order_by('?').first()
    elif qs.exists():
        bank_q = qs.order_by('?').first()
    else:
        return None

    return {
        "question": bank_q.question_text,
        "category": bank_q.category,
        "topic": bank_q.category.replace('_', ' ').title(),
        "difficulty": bank_q.difficulty,
        "expected_answer": bank_q.expected_answer,
        "code_snippet": bank_q.code_snippet,
        "follow_up_hint": bank_q.follow_up_hint,
        "is_technical": True,
        "bank_question": bank_q,
        "is_follow_up": False,
        "is_demo": False
    }


def generate_next_interview_question(interview, previous_qa: list) -> dict:
    """
    Main question generation entrypoint.
    Branches cleanly based on interview_type:
    - 'hr': 100% HR questions
    - 'technical': 100% technical questions
    - 'combined': Planned mixture (~30% HR, ~70% Technical)
    """
    question_index = len(previous_qa) + 1
    total_questions = interview.question_count
    role = interview.custom_job_role
    interview_type = interview.interview_type

    # Determine whether this question should be HR or Technical
    should_ask_hr = False
    if interview_type == 'hr':
        should_ask_hr = True
    elif interview_type == 'technical':
        should_ask_hr = False
    elif interview_type == 'combined':
        should_ask_hr = is_combined_stage_hr(question_index, total_questions)

    # 1. HR Question generation
    if should_ask_hr:
        return _generate_hr_question(interview, previous_qa, question_index, total_questions)

    # 2. Technical Question generation
    return _generate_technical_question(interview, previous_qa, question_index, total_questions)


def _generate_hr_question(interview, previous_qa: list, question_index: int, total_questions: int) -> dict:
    """
    Generates an HR question using Gemini or fallback mock engine with strict HR guardrails.
    """
    role = interview.custom_job_role
    client = get_gemini_client()

    if not client:
        res = generate_mock_question(role, question_index, total_questions, previous_qa)
        res['is_technical'] = False
        res['topic'] = 'Behavioral'
        res['difficulty'] = interview.difficulty
        res['is_demo'] = True
        return res

    prompt = build_question_prompt(
        job_role=role,
        experience_level=interview.experience_level,
        difficulty=interview.difficulty,
        question_number=question_index,
        total_questions=total_questions,
        previous_qa=previous_qa,
        focus=interview.interview_focus,
        job_desc=interview.job_description,
        resume=interview.resume_text
    )

    for attempt in range(2):
        try:
            model_name = getattr(settings, 'GEMINI_MODEL', 'gemini-3.5-flash-lite')
            from google.genai import types

            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=HR_SYSTEM_INSTRUCTION,
                    response_mime_type="application/json",
                    temperature=0.7,
                )
            )
            raw_text = response.text.strip()
            data = json.loads(raw_text)
            question_text = data.get('question', '').strip()
            category = data.get('category', 'behavioral')
            is_followup = bool(data.get('is_follow_up', False))

            clean_q, cat = sanitize_or_replace_question(question_text, role, question_index)
            return {
                "question": clean_q,
                "category": cat or category,
                "topic": "Behavioral",
                "difficulty": interview.difficulty,
                "expected_answer": "",
                "code_snippet": "",
                "is_technical": False,
                "bank_question": None,
                "is_follow_up": is_followup,
                "is_demo": False
            }
        except Exception as e:
            logger.warning(f"Gemini HR question attempt {attempt+1} failed: {e}")

    res = generate_mock_question(role, question_index, total_questions, previous_qa)
    res['is_technical'] = False
    res['topic'] = 'Behavioral'
    res['difficulty'] = interview.difficulty
    res['is_demo'] = True
    return res


def _generate_technical_question(interview, previous_qa: list, question_index: int, total_questions: int) -> dict:
    """
    Generates or retrieves a technical question:
    1. First attempts to fetch from stored QuestionBank (excluding already asked questions).
    2. If bank exhausted or custom role not in bank, uses Gemini to dynamically generate role-specific technical question.
    3. If Gemini is unavailable, uses role fallback.
    """
    role = interview.custom_job_role

    # IDs of bank questions already asked in this interview session
    already_asked_bank_ids = list(
        interview.questions.filter(bank_question__isnull=False).values_list('bank_question_id', flat=True)
    )

    bank_result = fetch_bank_question(interview, exclude_question_ids=already_asked_bank_ids)
    if bank_result:
        return bank_result

    # If no stored bank question found (e.g. custom role or bank exhausted): generate via Gemini
    client = get_gemini_client()
    selected_techs = interview.selected_technologies or []
    tech_str = ", ".join(selected_techs) if selected_techs else None

    if not client:
        # Fallback for custom role
        return {
            "question": f"As a {role}, how do you approach architecture and design trade-offs when optimizing system throughput and handling runtime edge cases?",
            "category": "system_design",
            "topic": "Architecture & Optimization",
            "difficulty": interview.difficulty,
            "expected_answer": "Should address modular decoupling, scalability, caching, and handling failure modes gracefully.",
            "code_snippet": "",
            "follow_up_hint": "How do you monitor and benchmark these optimizations?",
            "is_technical": True,
            "bank_question": None,
            "is_follow_up": False,
            "is_demo": True
        }

    prompt = build_technical_question_prompt(
        job_role=role,
        experience_level=interview.experience_level,
        difficulty=interview.difficulty,
        question_number=question_index,
        total_questions=total_questions,
        previous_qa=previous_qa,
        technology=tech_str,
        job_desc=interview.job_description
    )

    for attempt in range(2):
        try:
            model_name = getattr(settings, 'GEMINI_MODEL', 'gemini-3.5-flash-lite')
            from google.genai import types

            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=TECHNICAL_SYSTEM_INSTRUCTION.format(job_role=role),
                    response_mime_type="application/json",
                    temperature=0.6,
                )
            )
            raw_text = response.text.strip()
            data = json.loads(raw_text)
            question_text = data.get('question', '').strip()

            if is_valid_technical_question(question_text):
                return {
                    "question": question_text,
                    "category": data.get('category', 'technical_problem_solving'),
                    "topic": data.get('topic', f'{role} Fundamentals'),
                    "difficulty": data.get('difficulty', interview.difficulty),
                    "expected_answer": data.get('expected_answer', ''),
                    "code_snippet": data.get('code_snippet', ''),
                    "follow_up_hint": data.get('follow_up_hint', ''),
                    "is_technical": True,
                    "bank_question": None,
                    "is_follow_up": bool(data.get('is_follow_up', False)),
                    "is_demo": False
                }
        except Exception as e:
            logger.warning(f"Gemini technical question attempt {attempt+1} failed: {e}")

    return {
        "question": f"In your role as a {role}, what core architectural principles do you prioritize to ensure code maintainability, performance, and testability?",
        "category": "architecture",
        "topic": "Core Architecture",
        "difficulty": interview.difficulty,
        "expected_answer": "Discuss modularity, separation of concerns, test isolation, and dependency management.",
        "code_snippet": "",
        "follow_up_hint": "How do you detect and refactor technical debt?",
        "is_technical": True,
        "bank_question": None,
        "is_follow_up": False,
        "is_demo": True
    }


def evaluate_candidate_answer(interview, question, answer_text: str) -> dict:
    """
    Evaluates candidate's answer based on whether the question is technical or HR.
    """
    is_technical = getattr(question, 'is_technical', False)
    role = interview.custom_job_role
    client = get_gemini_client()

    # Route to technical evaluation
    if is_technical:
        expected = getattr(question, 'expected_answer', '')
        topic = getattr(question, 'topic', '')

        if not client:
            res = evaluate_mock_technical_answer(role, question.question_text, answer_text, expected_answer=expected)
            res['is_technical'] = True
            res['is_demo'] = True
            return res

        prompt = build_technical_evaluation_prompt(
            job_role=role,
            experience_level=interview.experience_level,
            question_text=question.question_text,
            answer_text=answer_text,
            expected_answer=expected,
            topic=topic
        )

        for attempt in range(2):
            try:
                model_name = getattr(settings, 'GEMINI_MODEL', 'gemini-3.5-flash-lite')
                from google.genai import types

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=TECHNICAL_SYSTEM_INSTRUCTION.format(job_role=role),
                        response_mime_type="application/json",
                        temperature=0.3,
                    )
                )
                raw_text = response.text.strip()
                data = json.loads(raw_text)

                acc = max(0.0, min(100.0, float(data.get('technical_accuracy_score', 75.0))))
                depth = max(0.0, min(100.0, float(data.get('technical_depth_score', 70.0))))
                ps = max(0.0, min(100.0, float(data.get('problem_solving_score', 70.0))))
                cla = max(0.0, min(100.0, float(data.get('clarity_score', 80.0))))

                overall = round((acc * 0.35) + (depth * 0.30) + (ps * 0.25) + (cla * 0.10), 1)

                return {
                    "is_technical": True,
                    "technical_accuracy_score": acc,
                    "technical_depth_score": depth,
                    "problem_solving_score": ps,
                    "clarity_score": cla,
                    "overall_score": overall,
                    "correct_points": data.get('correct_points', ["Addressed core technical premise"]),
                    "missing_points": data.get('missing_points', ["Could detail edge conditions and performance nuances"]),
                    "correct_answer_explanation": data.get('correct_answer_explanation', expected or "Comprehensive solution."),
                    "what_went_well": data.get('what_went_well', "Good technical understanding."),
                    "what_could_improve": data.get('what_could_improve', "Deepen discussion of edge cases and syntax precision."),
                    "improvement_suggestions": data.get('improvement_suggestions', "Provide concrete code patterns and computational complexity."),
                    "suggested_answer_structure": data.get('suggested_answer_structure', "Structure: Mechanism -> Syntax -> Failure Scenarios."),
                    "score_explanation": data.get('score_explanation', "Evaluated according to technical accuracy and depth."),
                    "is_demo": False
                }
            except Exception as e:
                logger.warning(f"Gemini technical evaluation attempt {attempt+1} failed: {e}")

        res = evaluate_mock_technical_answer(role, question.question_text, answer_text, expected_answer=expected)
        res['is_technical'] = True
        res['is_demo'] = True
        return res

    # HR evaluation
    if not client:
        res = evaluate_mock_answer(role, question.question_text, answer_text)
        res['is_technical'] = False
        res['is_demo'] = True
        return res

    prompt = build_evaluation_prompt(
        job_role=role,
        experience_level=interview.experience_level,
        question_text=question.question_text,
        answer_text=answer_text
    )

    for attempt in range(2):
        try:
            model_name = getattr(settings, 'GEMINI_MODEL', 'gemini-3.5-flash-lite')
            from google.genai import types

            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=HR_SYSTEM_INSTRUCTION,
                    response_mime_type="application/json",
                    temperature=0.3,
                )
            )
            raw_text = response.text.strip()
            data = json.loads(raw_text)

            rel = max(0.0, min(100.0, float(data.get('relevance_score', 70.0))))
            cla = max(0.0, min(100.0, float(data.get('clarity_score', 70.0))))
            ex = max(0.0, min(100.0, float(data.get('examples_score', 65.0))))
            com = max(0.0, min(100.0, float(data.get('communication_score', 75.0))))

            overall = round((rel * 0.30) + (cla * 0.25) + (ex * 0.25) + (com * 0.20), 1)

            return {
                "is_technical": False,
                "relevance_score": rel,
                "clarity_score": cla,
                "examples_score": ex,
                "communication_score": com,
                "overall_score": overall,
                "what_went_well": data.get('what_went_well', 'Clear response.'),
                "what_could_improve": data.get('what_could_improve', 'Provide more supporting examples.'),
                "improvement_suggestions": data.get('improvement_suggestions', 'Use the STAR technique.'),
                "suggested_answer_structure": data.get('suggested_answer_structure', 'Example: Situation -> Task -> Action -> Result'),
                "score_explanation": data.get('score_explanation', 'Evaluation based on HR criteria.'),
                "is_demo": False
            }
        except Exception as e:
            logger.warning(f"Gemini HR evaluation attempt {attempt+1} failed: {e}")

    res = evaluate_mock_answer(role, question.question_text, answer_text)
    res['is_technical'] = False
    res['is_demo'] = True
    return res


def synthesize_interview_report(interview, qa_eval_list: list) -> dict:
    """
    Synthesizes overall report for the completed interview session.
    Calculates separate HR and Technical score aggregates and feedback.
    """
    role = interview.custom_job_role
    interview_type = interview.interview_type
    client = get_gemini_client()

    if not client or not qa_eval_list:
        res = generate_mock_report(role, interview.experience_level, qa_eval_list, interview_type=interview_type)
        res['is_demo'] = True
        return res

    prompt = build_report_prompt(
        job_role=role,
        experience_level=interview.experience_level,
        qa_eval_list=qa_eval_list,
        interview_type=interview_type
    )

    sys_inst = COMBINED_SYSTEM_INSTRUCTION.format(job_role=role) if interview_type == 'combined' else (
        TECHNICAL_SYSTEM_INSTRUCTION.format(job_role=role) if interview_type == 'technical' else HR_SYSTEM_INSTRUCTION
    )

    for attempt in range(2):
        try:
            model_name = getattr(settings, 'GEMINI_MODEL', 'gemini-3.5-flash-lite')
            from google.genai import types

            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=sys_inst,
                    response_mime_type="application/json",
                    temperature=0.4,
                )
            )
            raw_text = response.text.strip()
            data = json.loads(raw_text)

            # Extract scores with fallback calculations
            hr_evals = [e for e in qa_eval_list if not e.get('is_technical', False)]
            tech_evals = [e for e in qa_eval_list if e.get('is_technical', False)]

            avg_hr = round(sum(e.get("overall_score", 0.0) for e in hr_evals) / len(hr_evals), 1) if hr_evals else None
            avg_tech = round(sum(e.get("overall_score", 0.0) for e in tech_evals) / len(tech_evals), 1) if tech_evals else None

            rep_hr_score = float(data.get('hr_score', avg_hr or 0.0))
            rep_tech_score = float(data.get('technical_score', avg_tech or 0.0))

            return {
                "summary": data.get('summary', f"Performance report for {role} ({interview_type.upper()})."),
                "hr_score": rep_hr_score,
                "technical_score": rep_tech_score,
                "overall_score": float(data.get('overall_score', round((rep_hr_score + rep_tech_score) / 2, 1) if rep_hr_score and rep_tech_score else (rep_hr_score or rep_tech_score))),
                "strengths": data.get('strengths', ["Good domain alignment", "Professional communication"]),
                "areas_for_improvement": data.get('areas_for_improvement', ["Use STAR structure", "Deepen technical edge-case handling"]),
                "hr_strengths": data.get('hr_strengths', ["Clear communication", "Good self-awareness"]),
                "hr_areas_for_improvement": data.get('hr_areas_for_improvement', ["Structure behavioral stories with quantifiable results"]),
                "technical_strengths": data.get('technical_strengths', ["Sound grasp of core mechanisms and syntax"]),
                "technical_areas_for_improvement": data.get('technical_areas_for_improvement', ["Consider scalability and error edge cases"]),
                "recommendations": data.get('recommendations', ["Practice timed questions and STAR stories"]),
                "recommended_topics": data.get('recommended_topics', ["System Design", "Behavioral Leadership"]),
                "sample_improved_answer": data.get('sample_improved_answer', ""),
                "is_demo": False
            }
        except Exception as e:
            logger.warning(f"Gemini report synthesis failed: {e}")

    res = generate_mock_report(role, interview.experience_level, qa_eval_list, interview_type=interview_type)
    res['is_demo'] = True
    return res
