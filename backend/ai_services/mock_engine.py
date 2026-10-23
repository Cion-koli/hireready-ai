"""
Deterministic Interview and Evaluation Engine for HireReady AI.
Used when GEMINI_API_KEY is not configured or as reliable fallback.
Supports HR Interview, Technical Interview, and Combined (HR + Technical) Interview modes.
"""

import re
from typing import Dict, Any, List

# Sequence of HR question templates for any custom role
ROLE_QUESTION_TEMPLATES = [
    {
        "category": "self_introduction",
        "template": "Hello! Welcome to your interview for the {role} position. To start off, could you introduce yourself and tell me what inspired you to pursue this career path?"
    },
    {
        "category": "motivation",
        "template": "What particularly appeals to you about stepping into this {role} role, and how do your background and personal strengths align with what an organization needs?"
    },
    {
        "category": "teamwork",
        "template": "In your experience as a {role}, can you share an example of a project where collaboration was essential? How did you ensure everyone stayed aligned and supported each other?"
    },
    {
        "category": "deadlines",
        "template": "Tight deadlines and shifting priorities are common for a {role}. Could you describe a time when you were under intense pressure to deliver, and how you managed your workload and stress?"
    },
    {
        "category": "conflict_resolution",
        "template": "Have you ever experienced a disagreement with a team member, manager, or stakeholder regarding a project decision in your work as a {role}? How did you approach the conversation to find common ground?"
    },
    {
        "category": "handling_feedback",
        "template": "Can you tell me about a time you received critical or constructive feedback from a supervisor on your performance as a {role}? What steps did you take to act on that feedback?"
    },
    {
        "category": "strengths_weaknesses",
        "template": "What do you consider your greatest professional asset as a {role}, and what is one skill or habit you are actively working on developing?"
    },
    {
        "category": "workplace_scenario",
        "template": "Imagine you are working on a key deliverable as a {role} and realize midway that the requirements given by the client or team lead are ambiguous. How would you handle the situation?"
    },
    {
        "category": "leadership",
        "template": "Even without a formal management title, individuals in a {role} often take ownership of situations. Can you share a time you demonstrated initiative or guided others through a complex challenge?"
    },
    {
        "category": "career_goals",
        "template": "Looking ahead, where do you see yourself professionally in the next 3 to 5 years, and how does this {role} opportunity fit into your long-term aspirations?"
    },
]


def generate_mock_question(role: str, question_index: int, total_questions: int, previous_qa: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Generates a role-personalized HR question or contextual follow-up.
    """
    if question_index > 1 and previous_qa:
        last_qa = previous_qa[-1]
        last_answer = last_qa.get('answer', '').strip().lower()

        if any(w in last_answer for w in ['team', 'colleague', 'manager', 'partner', 'stakeholder']):
            return {
                "question": f"Building on what you mentioned about collaborating with your colleagues, how do you handle situations where a team member isn't pulling their weight or communication breaks down as a {role}?",
                "category": "teamwork_followup",
                "is_follow_up": True
            }
        elif any(w in last_answer for w in ['deadline', 'pressure', 'late', 'urgent', 'time']):
            return {
                "question": f"You mentioned managing time constraints—could you share specifically how you communicate delays or negotiate realistic expectations with stakeholders when you realize a deadline is at risk as a {role}?",
                "category": "deadlines_followup",
                "is_follow_up": True
            }
        elif any(w in last_answer for w in ['learned', 'mistake', 'feedback', 'difficult', 'improve']):
            return {
                "question": f"That's a helpful perspective. Looking back at that situation, is there anything you would do differently today with the experience you've gained as a {role}?",
                "category": "reflection_followup",
                "is_follow_up": True
            }

    idx = (question_index - 1) % len(ROLE_QUESTION_TEMPLATES)
    item = ROLE_QUESTION_TEMPLATES[idx]
    question_text = item["template"].format(role=role)

    return {
        "question": question_text,
        "category": item["category"],
        "is_follow_up": False
    }


def evaluate_mock_answer(role: str, question_text: str, answer_text: str) -> Dict[str, Any]:
    """
    Evaluates candidate's answer with standard HR rubric:
    Relevance: 30%, Clarity: 25%, Examples/STAR: 25%, Communication: 20%
    """
    words = answer_text.strip().split()
    word_count = len(words)

    if word_count < 10:
        return {
            "relevance_score": 40.0,
            "clarity_score": 45.0,
            "examples_score": 25.0,
            "communication_score": 50.0,
            "overall_score": 38.8,
            "what_went_well": "You provided an initial thought, but the response was too brief to fully evaluate.",
            "what_could_improve": "HR interviewers look for structured, narrative responses with real context.",
            "improvement_suggestions": "Aim for at least 3 to 4 sentences explaining the situation, your actions, and the outcome (STAR method).",
            "suggested_answer_structure": f"Example structure: 'When working as a {role}, I faced [Situation]. My responsibility was [Task]. I decided to [Action], which resulted in [Result].'",
            "score_explanation": "Response was under 10 words, lacking sufficient detail for a professional HR evaluation."
        }

    if word_count < 40:
        has_star_words = any(w in answer_text.lower() for w in ['because', 'result', 'example', 'achieved', 'situation'])
        star_bonus = 10.0 if has_star_words else 0.0

        rel = min(75.0, 55.0 + word_count * 0.5)
        cla = min(78.0, 60.0 + word_count * 0.4)
        ex = min(70.0, 45.0 + star_bonus + word_count * 0.3)
        com = min(80.0, 65.0 + word_count * 0.3)
        overall = round((rel * 0.30) + (cla * 0.25) + (ex * 0.25) + (com * 0.20), 1)

        return {
            "relevance_score": rel,
            "clarity_score": cla,
            "examples_score": ex,
            "communication_score": com,
            "overall_score": overall,
            "what_went_well": f"Directly touched upon the question in relation to the {role} context.",
            "what_could_improve": "Needs more concrete supporting details and clear explanation of the impact of your actions.",
            "improvement_suggestions": "Adopt the STAR framework: clearly separate Situation, Task, Action, and the final Result.",
            "suggested_answer_structure": f"Example enhancement: 'In a previous project, our team faced a tight timeline. I took initiative by organizing daily check-ins, allowing us to deliver 2 days ahead of schedule.'",
            "score_explanation": "Answer was direct and relevant, but brief. Expanding on measurable outcomes will significantly raise your score."
        }

    has_star = any(w in answer_text.lower() for w in ['situation', 'task', 'action', 'result', 'outcome', 'learned', 'team', 'delivered', 'achieved'])
    rel = 88.0 if has_star else 80.0
    cla = 85.0
    ex = 86.0 if has_star else 76.0
    com = 88.0
    overall = round((rel * 0.30) + (cla * 0.25) + (ex * 0.25) + (com * 0.20), 1)

    return {
        "relevance_score": rel,
        "clarity_score": cla,
        "examples_score": ex,
        "communication_score": com,
        "overall_score": overall,
        "what_went_well": f"Well-articulated response demonstrating strong behavioral awareness for a {role}.",
        "what_could_improve": "Highlight tangible metrics or specific long-term takeaways where applicable.",
        "improvement_suggestions": "Quantify your impact when possible (e.g. 'reduced escalations by 25%' or 'saved 3 hours per sprint').",
        "suggested_answer_structure": "Your answer followed good structure. You can polish it further by concluding with what this experience taught you for future challenges.",
        "score_explanation": f"Strong demonstration of professional communication and role-relevant problem solving for a {role}."
    }


def evaluate_mock_technical_answer(role: str, question_text: str, answer_text: str, expected_answer: str = "", rubric: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Evaluates candidate's technical answer using the Technical Rubric:
    Technical Accuracy: 35%, Depth: 30%, Problem Solving: 25%, Clarity: 10%
    """
    words = answer_text.strip().split()
    word_count = len(words)

    # Empty or super short answer
    if word_count < 8:
        return {
            "technical_accuracy_score": 35.0,
            "technical_depth_score": 30.0,
            "problem_solving_score": 30.0,
            "clarity_score": 45.0,
            "overall_score": 33.3,
            "correct_points": ["Attempted to answer the prompt."],
            "missing_points": [
                "Lacks core technical concepts and direct mechanism explanations.",
                "Did not provide necessary code, query syntax, or architectural trade-offs."
            ],
            "correct_answer_explanation": expected_answer or "A complete technical answer should explain the core principles, syntax/mechanics, and practical trade-offs.",
            "what_went_well": "Prompt received an initial response.",
            "what_could_improve": "Technical interviews require detailed explanations, architectural rationale, and syntax when applicable.",
            "improvement_suggestions": "State the underlying mechanism, time/space complexity, and practical edge cases.",
            "suggested_answer_structure": f"Model Answer: {expected_answer[:250]}..." if expected_answer else "Model Answer: Explain definition -> Internal mechanism -> Example code -> Trade-offs.",
            "score_explanation": "Answer was too brief to demonstrate technical competence on this topic."
        }

    # Moderate answer (8-30 words)
    if word_count < 30:
        has_keywords = False
        if expected_answer:
            exp_keywords = [w.lower() for w in re.findall(r'\b[a-zA-Z]{4,}\b', expected_answer)]
            matched_kw = [k for k in exp_keywords if k in answer_text.lower()]
            has_keywords = len(matched_kw) >= 2

        acc = min(75.0, 55.0 + (15.0 if has_keywords else 5.0))
        depth = min(70.0, 50.0 + word_count * 0.5)
        ps = min(72.0, 52.0 + word_count * 0.5)
        clarity = 75.0
        overall = round((acc * 0.35) + (depth * 0.30) + (ps * 0.25) + (clarity * 0.10), 1)

        return {
            "technical_accuracy_score": acc,
            "technical_depth_score": depth,
            "problem_solving_score": ps,
            "clarity_score": clarity,
            "overall_score": overall,
            "correct_points": [
                "Identified the relevant high-level domain or concept.",
                "Demonstrated fundamental awareness of the technical problem."
            ],
            "missing_points": [
                "Could elaborate on underlying runtime/database behavior or edge cases.",
                "Did not discuss performance impact or trade-offs with alternative approaches."
            ],
            "correct_answer_explanation": expected_answer or "Technical solutions should cover internal behavior, error states, and algorithmic efficiency.",
            "what_went_well": "Accurately noted the core subject matter.",
            "what_could_improve": "Expand on the specific keywords, internal execution flow, and handling of failure scenarios.",
            "improvement_suggestions": "Mention how this feature is used in high-scale production systems.",
            "suggested_answer_structure": f"Key points to include: {expected_answer[:220]}..." if expected_answer else "Structure: Definition -> Syntax/Code -> Common Pitfalls.",
            "score_explanation": "Good foundational response with room for deeper technical precision."
        }

    # In-depth technical answer (30+ words)
    has_code_or_structure = any(ch in answer_text for ch in ['(', ')', '{', '}', ';', '=', 'SELECT', 'def ', 'function', 'class'])
    acc = 88.0 if has_code_or_structure else 82.0
    depth = 85.0
    ps = 86.0 if has_code_or_structure else 80.0
    clarity = 88.0
    overall = round((acc * 0.35) + (depth * 0.30) + (ps * 0.25) + (clarity * 0.10), 1)

    return {
        "technical_accuracy_score": acc,
        "technical_depth_score": depth,
        "problem_solving_score": ps,
        "clarity_score": clarity,
        "overall_score": overall,
        "correct_points": [
            "Sound conceptual foundation and thorough technical explanation.",
            "Addressed key architectural mechanisms and proper terminology."
        ],
        "missing_points": [
            "Consider discussing concrete memory allocation nuances or edge constraints for full mastery."
        ],
        "correct_answer_explanation": expected_answer or "A robust technical answer covers data structures, syntax accuracy, and scalability constraints.",
        "what_went_well": f"Demonstrated comprehensive technical command suitable for a {role}.",
        "what_could_improve": "Highlight specific production telemetry or benchmarking strategies where applicable.",
        "improvement_suggestions": "Continue providing concrete code patterns and computational complexity analysis.",
        "suggested_answer_structure": "Your answer structure was well-organized with clear engineering reasoning.",
        "score_explanation": f"Strong technical response reflecting solid practical competence for a {role}."
    }


def generate_mock_report(role: str, experience_level: str, evaluations: List[Dict[str, Any]], interview_type: str = "hr") -> Dict[str, Any]:
    """
    Synthesizes overall report from individual evaluations.
    Separates HR and Technical scores and feedback for combined interviews.
    """
    if not evaluations:
        return {
            "summary": f"Practice interview for {role} ({interview_type}) was ended before any answers were recorded.",
            "hr_score": 0.0,
            "technical_score": 0.0,
            "overall_score": 0.0,
            "strengths": ["Interview setup completed"],
            "areas_for_improvement": ["Complete at least 3-5 questions to receive comprehensive evaluation"],
            "hr_strengths": ["Willingness to practice"],
            "hr_areas_for_improvement": ["Provide structured behavioral responses"],
            "technical_strengths": ["Setup completed"],
            "technical_areas_for_improvement": ["Submit code and conceptual answers to test technical proficiency"],
            "recommendations": ["Re-attempt the interview and submit responses to build your profile"],
            "recommended_topics": ["Core fundamentals", "Communication scenarios"],
            "sample_improved_answer": "N/A"
        }

    # Separate HR vs Technical evaluations
    hr_evals = [e for e in evaluations if not e.get('is_technical', False)]
    tech_evals = [e for e in evaluations if e.get('is_technical', False)]

    avg_overall = round(sum(e.get("overall_score", 0.0) for e in evaluations) / len(evaluations), 1)
    avg_hr = round(sum(e.get("overall_score", 0.0) for e in hr_evals) / len(hr_evals), 1) if hr_evals else avg_overall
    avg_tech = round(sum(e.get("overall_score", 0.0) for e in tech_evals) / len(tech_evals), 1) if tech_evals else avg_overall

    is_combined = interview_type == 'combined'
    is_tech = interview_type == 'technical'

    summary_text = (
        f"Candidate completed {len(evaluations)} question(s) for the {role} ({experience_level}) {interview_type.upper()} round. "
        f"Overall practice score: {avg_overall}%. "
        + (f"HR Score: {avg_hr}% | Technical Score: {avg_tech}%. " if is_combined else "")
        + "Clear demonstration of core domain knowledge with targeted opportunities for improvement."
    )

    return {
        "summary": summary_text,
        "hr_score": avg_hr,
        "technical_score": avg_tech,
        "overall_score": avg_overall,
        "strengths": [
            f"Strong professional communication tailored to the {role} domain",
            "Clear technical reasoning and structured approach to problem solving",
            "Honest reflection on workplace challenges and technical trade-offs"
        ],
        "areas_for_improvement": [
            "Ensure code and query answers consider edge cases and boundary conditions",
            "Use the STAR framework consistently on behavioral scenarios",
            "Quantify past project impact with concrete metrics"
        ],
        "hr_strengths": [
            "Polite, respectful, and articulate communication",
            "Demonstrated enthusiasm for the role and collaborative teamwork"
        ],
        "hr_areas_for_improvement": [
            "Provide more specific examples of resolving conflicts with stakeholders",
            "Articulate 3-year career goals with clearer milestone definitions"
        ],
        "technical_strengths": [
            f"Accurate understanding of {role} fundamentals and architecture",
            "Clear articulation of internal runtime behavior and database mechanisms"
        ],
        "technical_areas_for_improvement": [
            "Deepen familiarity with concurrency, edge cases, and query tuning",
            "Write cleaner, more idiomatic code with explicit error handling"
        ],
        "recommendations": [
            "Practice writing SQL queries and algorithm snippets under timed conditions",
            "Prepare 3 STAR stories focused on cross-functional technical leadership",
            f"Review advanced {role} architecture and system design patterns"
        ],
        "recommended_topics": [
            "System Architecture & Scaling",
            "Database Indexing & Isolation Levels",
            "Handling Ambiguous Requirements & Team Alignment"
        ],
        "sample_improved_answer": (
            f"Model Technical Answer for {role}: 'When designing for scalability, I isolate data access layers, "
            f"implement covering indexes to avoid table lookups, and apply connection pooling with backpressure. "
            f"This maintains sub-50ms p95 latencies and prevents resource exhaustion during sudden traffic spikes.'"
        )
    }
