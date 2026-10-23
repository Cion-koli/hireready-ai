"""
Guardrail Validators for HireReady AI.
Validates HR questions against accidental technical leaks,
and validates technical questions against generic behavioral filler.
"""

import re

# Technical patterns that indicate a technical quiz or coding question
DISALLOWED_TECHNICAL_PATTERNS = [
    r'\bwrite\s+(a\s+)?([a-zA-Z0-9_#\+\.\-]+\s+)?(code|program|script|function|query|sql|class|method|snippet)\b',
    r'\b(write|code|implement|program)\s+(in\s+)?(python|javascript|react|vue|angular|java|c\+\+|c#|go|rust|sql|html|css|php|ruby)\b',
    r'\b(syntax|time complexity|space complexity|big o|o\(n\)|algorithm)\b',
    r'\b(leetcode|binary search|linked list|binary tree|dynamic programming|data structure)\b',
    r'\b(select\s+\*|insert\s+into|drop\s+table|foreign\s+key\s+syntax|sql\s+query)\b',
    r'\b(regex|regular expression pattern|pointer|memory leak|garbage collector syntax)\b',
    r'\bexplain the difference between let and var\b',
    r'\bexplain the difference between (deep|shallow) copy\b',
    r'\b(math formula|solve the following equation|aptitude puzzle)\b',
    r'\b(what is the output of the following|debug this snippet)\b',
    r'\b(parse\s+json|parse\s+xml|rest\s+api\s+syntax)\b',
]

TECHNICAL_REGEX = re.compile('|'.join(DISALLOWED_TECHNICAL_PATTERNS), re.IGNORECASE)

# Behavioral patterns that indicate a generic HR question
GENERIC_HR_PATTERNS = [
    r'\btell me about yourself\b',
    r'\bwhat (are|is) your greatest strength(s)?\b',
    r'\bwhat is your greatest weakness\b',
    r'\bwhere do you see yourself in (3|5) years\b',
    r'\bwhy do you want to work (at|for) (us|our company|this company)\b',
    r'\bhow do you handle conflict with a coworker\b',
]

GENERIC_HR_REGEX = re.compile('|'.join(GENERIC_HR_PATTERNS), re.IGNORECASE)

# Valid HR Categories
VALID_HR_CATEGORIES = [
    'self_introduction',
    'motivation',
    'teamwork',
    'deadlines',
    'conflict_resolution',
    'strengths_weaknesses',
    'handling_feedback',
    'workplace_scenario',
    'career_goals',
    'leadership',
    'adaptability'
]

# Curated fallback HR templates personalized by job role
HR_ROLE_FALLBACK_QUESTIONS = [
    ("Tell me about yourself, your background, and what drew you specifically to a career as a {role}?", "self_introduction"),
    ("As a {role}, how do you prioritize competing deadlines when multiple urgent tasks land on your desk?", "deadlines"),
    ("Can you share a situation where you had to collaborate closely with a team or non-technical stakeholders to deliver a project as a {role}?", "teamwork"),
    ("Tell me about a time you encountered constructive feedback or criticism on your work. How did you react and improve?", "handling_feedback"),
    ("What would you say are your greatest strengths, and what is one area you are currently striving to improve as a {role}?", "strengths_weaknesses"),
    ("Describe a workplace challenge or disagreement with a colleague or manager, and how you worked towards a professional resolution.", "conflict_resolution"),
    ("Why are you interested in joining our organization for this {role} position, and where do you envision your career in 3 to 5 years?", "career_goals"),
    ("Tell me about a time when project requirements changed abruptly. How did you adapt your workflow to stay on track?", "adaptability"),
]


def is_valid_hr_question(question_text: str) -> bool:
    """
    Returns True if question_text is clean and strictly HR-focused.
    Returns False if it asks for code, syntax, technical tests, or aptitude math.
    """
    if not question_text or len(question_text.strip()) < 10:
        return False
    
    # Check against technical pattern regex
    if TECHNICAL_REGEX.search(question_text):
        return False

    return True


def sanitize_or_replace_question(question_text: str, role: str, question_index: int = 1) -> tuple[str, str]:
    """
    Validates an HR question. If invalid or technical, returns a role-personalized HR fallback.
    Returns: (clean_question_text, category)
    """
    if is_valid_hr_question(question_text):
        return question_text.strip(), "behavioral"

    # Select fallback based on question order
    idx = (question_index - 1) % len(HR_ROLE_FALLBACK_QUESTIONS)
    template, cat = HR_ROLE_FALLBACK_QUESTIONS[idx]
    clean_question = template.format(role=role)
    return clean_question, cat


def is_valid_technical_question(question_text: str) -> bool:
    """
    Returns True if question_text is a genuine technical inquiry and not an HR placeholder.
    """
    if not question_text or len(question_text.strip()) < 15:
        return False

    # If it matches purely generic HR tropes like "tell me about yourself", reject as technical question
    if GENERIC_HR_REGEX.search(question_text):
        return False

    return True
