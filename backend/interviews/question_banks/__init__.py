"""
Question Banks aggregation module.
Exposes all predefined questions and helper functions to validate question counts per role and per technology.
"""

from .software_engineer_python import SOFTWARE_ENGINEER_PYTHON_QUESTIONS
from .software_engineer_html import SOFTWARE_ENGINEER_HTML_QUESTIONS
from .software_engineer_css import SOFTWARE_ENGINEER_CSS_QUESTIONS
from .software_engineer_javascript import SOFTWARE_ENGINEER_JAVASCRIPT_QUESTIONS
from .software_engineer_sql import SOFTWARE_ENGINEER_SQL_QUESTIONS

from .python_developer import PYTHON_DEVELOPER_QUESTIONS
from .frontend_developer import FRONTEND_DEVELOPER_QUESTIONS
from .backend_developer import BACKEND_DEVELOPER_QUESTIONS
from .fullstack_developer import FULLSTACK_DEVELOPER_QUESTIONS
from .java_developer import JAVA_DEVELOPER_QUESTIONS
from .react_developer import REACT_DEVELOPER_QUESTIONS
from .sql_developer import SQL_DEVELOPER_QUESTIONS
from .data_analyst import DATA_ANALYST_QUESTIONS
from .qa_tester import QA_TESTER_QUESTIONS
from .devops_engineer import DEVOPS_ENGINEER_QUESTIONS
from .cybersecurity_analyst import CYBERSECURITY_ANALYST_QUESTIONS

SOFTWARE_ENGINEER_QUESTIONS = (
    SOFTWARE_ENGINEER_PYTHON_QUESTIONS +
    SOFTWARE_ENGINEER_HTML_QUESTIONS +
    SOFTWARE_ENGINEER_CSS_QUESTIONS +
    SOFTWARE_ENGINEER_JAVASCRIPT_QUESTIONS +
    SOFTWARE_ENGINEER_SQL_QUESTIONS
)

ALL_PREDEFINED_QUESTIONS = (
    SOFTWARE_ENGINEER_QUESTIONS +
    PYTHON_DEVELOPER_QUESTIONS +
    FRONTEND_DEVELOPER_QUESTIONS +
    BACKEND_DEVELOPER_QUESTIONS +
    FULLSTACK_DEVELOPER_QUESTIONS +
    JAVA_DEVELOPER_QUESTIONS +
    REACT_DEVELOPER_QUESTIONS +
    SQL_DEVELOPER_QUESTIONS +
    DATA_ANALYST_QUESTIONS +
    QA_TESTER_QUESTIONS +
    DEVOPS_ENGINEER_QUESTIONS +
    CYBERSECURITY_ANALYST_QUESTIONS
)

ROLE_QUESTION_BANKS = {
    "Software Engineer": SOFTWARE_ENGINEER_QUESTIONS,
    "Python Developer": PYTHON_DEVELOPER_QUESTIONS,
    "Frontend Developer": FRONTEND_DEVELOPER_QUESTIONS,
    "Backend Developer": BACKEND_DEVELOPER_QUESTIONS,
    "Full-Stack Developer": FULLSTACK_DEVELOPER_QUESTIONS,
    "Java Developer": JAVA_DEVELOPER_QUESTIONS,
    "React Developer": REACT_DEVELOPER_QUESTIONS,
    "SQL Developer": SQL_DEVELOPER_QUESTIONS,
    "Data Analyst": DATA_ANALYST_QUESTIONS,
    "QA / Software Tester": QA_TESTER_QUESTIONS,
    "DevOps Engineer": DEVOPS_ENGINEER_QUESTIONS,
    "Cybersecurity Analyst": CYBERSECURITY_ANALYST_QUESTIONS,
}

SOFTWARE_ENGINEER_TECH_BANKS = {
    "python": SOFTWARE_ENGINEER_PYTHON_QUESTIONS,
    "html": SOFTWARE_ENGINEER_HTML_QUESTIONS,
    "css": SOFTWARE_ENGINEER_CSS_QUESTIONS,
    "javascript": SOFTWARE_ENGINEER_JAVASCRIPT_QUESTIONS,
    "sql": SOFTWARE_ENGINEER_SQL_QUESTIONS,
}


def validate_question_banks():
    """
    Validates minimum counts:
    - At least 25 questions per technical role.
    - At least 125 questions for Software Engineer (at least 25 each for Python, HTML, CSS, JavaScript, SQL).
    Returns (is_valid, report_dict).
    """
    report = {"roles": {}, "software_engineer_techs": {}, "total": len(ALL_PREDEFINED_QUESTIONS), "is_valid": True}

    for role_name, q_list in ROLE_QUESTION_BANKS.items():
        count = len(q_list)
        min_required = 125 if role_name == "Software Engineer" else 25
        valid = count >= min_required
        report["roles"][role_name] = {"count": count, "min_required": min_required, "valid": valid}
        if not valid:
            report["is_valid"] = False

    for tech, q_list in SOFTWARE_ENGINEER_TECH_BANKS.items():
        count = len(q_list)
        valid = count >= 25
        report["software_engineer_techs"][tech] = {"count": count, "min_required": 25, "valid": valid}
        if not valid:
            report["is_valid"] = False

    return report["is_valid"], report
