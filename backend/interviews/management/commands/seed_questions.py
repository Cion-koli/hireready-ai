"""
Django management command to seed the QuestionBank database with verified technical questions.
Validates that every technical role has at least 25 questions, and Software Engineer has at least 125 questions (25 per technology).
"""

from django.core.management.base import BaseCommand, CommandError
from interviews.models import QuestionBank
from interviews.question_banks import (
    ALL_PREDEFINED_QUESTIONS,
    validate_question_banks,
    ROLE_QUESTION_BANKS,
    SOFTWARE_ENGINEER_TECH_BANKS,
)


class Command(BaseCommand):
    help = "Populates QuestionBank with verified technical questions and validates counts."

    def add_arguments(self, parser):
        parser.add_argument(
            "--validate-only",
            action="store_true",
            help="Validate question bank counts without inserting into database",
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Validating question bank counts..."))
        is_valid, report = validate_question_banks()

        self.stdout.write(f"\n--- Technical Roles Summary ({len(report['roles'])} roles) ---")
        for role, data in report["roles"].items():
            status = self.style.SUCCESS("[OK]") if data["valid"] else self.style.ERROR("[FAIL]")
            self.stdout.write(f"  {status} {role}: {data['count']} questions (Min required: {data['min_required']})")

        self.stdout.write("\n--- Software Engineer Technology Coverage (5 technologies) ---")
        for tech, data in report["software_engineer_techs"].items():
            status = self.style.SUCCESS("[OK]") if data["valid"] else self.style.ERROR("[FAIL]")
            self.stdout.write(f"  {status} {tech.upper()}: {data['count']} questions (Min required: {data['min_required']})")

        self.stdout.write(f"\nTotal verified questions in bank: {report['total']}\n")

        if not is_valid:
            raise CommandError("Question bank validation failed! One or more roles/technologies are below minimum.")

        if options["validate_only"]:
            self.stdout.write(self.style.SUCCESS("Validation successful! (Validate-only mode)"))
            return

        self.stdout.write(self.style.NOTICE("Seeding questions into database..."))
        created_count = 0
        updated_count = 0

        for q in ALL_PREDEFINED_QUESTIONS:
            obj, created = QuestionBank.objects.update_or_create(
                role=q["role"],
                question_text=q["question_text"],
                defaults={
                    "technology": q.get("technology") or "",
                    "category": q.get("category") or "",
                    "difficulty": q.get("difficulty") or "medium",
                    "expected_answer": q.get("expected_answer") or "",
                    "rubric": q.get("rubric") or {},
                    "code_snippet": q.get("code_snippet") or "",
                    "follow_up_hint": q.get("follow_up_hint") or "",
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        total_db = QuestionBank.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f"Successfully seeded QuestionBank: {created_count} created, {updated_count} updated. Total in DB: {total_db}"
        ))
