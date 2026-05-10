from fpdf import FPDF
import os
import re

def sanitize_for_pdf(text):
    """Replace emojis with ASCII training tags & strip non-PDF-safe chars"""
    emoji_map = {
        '🎯': '[GOAL]', '⏱️': '[TIME]', '📊': '[CHART]', '✅': '[OK]',
        '💡': '[TIP]', '⚠️': '[WARN]', '📁': '[FOLDER]', '🚀': '[START]',
        '📖': '[DOC]', '🛠️': '[TOOL]', '📦': '[PKG]', '💬': '[Q&A]',
        '🔜': '[NEXT]', '🔹': '•', '🏆': '[WIN]', '❌': '[FAIL]',
        '📍': '[LOC]', '🎤': '[ASK]', '🌍': '[ENV]', '⏱': '[TIME]'
    }
    for emo, tag in emoji_map.items():
        text = text.replace(emo, tag)
    # Remove any remaining non-ASCII characters
    return re.sub(r'[^\x00-\x7F]+', ' ', text).strip()
    # Clean up multiple spaces
    return re.sub(r'\s+', ' ', sanitized).strip()

class TrainerNotesPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "Python Functions & Advanced Concepts - Trainer Notes", 0, 1, "C")
        self.line(10, 18, 200, 18)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")

    def add_slide_note(self, slide_num, title, note):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(240, 248, 255)  # Light blue header
        self.cell(0, 8, f"Slide {slide_num}: {title}", 0, 1, "L", fill=True)
        self.ln(2)
        self.set_font("Helvetica", "", 10)
        # Sanitize before writing to PDF
        self.multi_cell(0, 5, sanitize_for_pdf(note))
        self.ln(4)

def main():
    pdf = TrainerNotesPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    notes = [
        (1, "Title Slide", "[GOAL] OPENING: Ask 'How many of you have copied-pasted the same 10-line script across projects?' Set the tone: Functions aren't just syntax—they're the backbone of maintainable automation frameworks. Emphasize that today's session directly translates to pytest fixtures, API clients, and CI utilities."),
        (2, "Session Agenda & Learning Goals", "[TIME] PACING: 60 mins total. Keep theory tight; spend 40% on live coding & 20% on hands-on. Highlight that each concept maps directly to test framework design. Ask participants to open their IDEs before Slide 4."),
        (3, "Why Functions? The Automation Multiplier", "[ASK] ENGAGEMENT: Show a 30-line script with duplicated login logic. Refactor it into a function live. Ask: 'What breaks if the auth endpoint changes in 5 files vs 1 function?' Connect to framework maintainability."),
        (4, "Parameters & Return Types", "[WARN] PITFALL: Learners ignore type hints. Stress that hints don't enforce types but enable linters (mypy, ruff) and prevent silent CI failures. Show IDE popup with `-> tuple[str, int]`. Relate to test data validation contracts."),
        (5, "Default & Keyword Arguments", "[ASK] ENGAGEMENT: Run `setup_browser()` vs `setup_browser(timeout=10)`. Ask: 'Why are defaults dangerous if they're mutable?' (Preview: lists/dicts). Show how keyword args make test steps self-documenting in CI logs."),
        (6, "*args: Variable Positional Arguments", "[TIP] AUTOMATION CONTEXT: Bulk test tagging, retry queues, error aggregation. Show how `args` prevents hardcoding test counts. Warn against mixing `*args` with positional-only params without care. Live demo: pass 2 vs 10 IDs."),
        (7, "**kwargs: Variable Keyword Arguments", "[GOAL] USE CASE: CI pipeline metadata, environment variables, API headers. Emphasize `.get()` for safe access. Show how frameworks pass `**kwargs` through layers (test -> driver -> API) without rewriting signatures."),
        (8, "Combining *args & **kwargs", "[WARN] ORDER MATTERS: Positional -> *args -> keyword -> **kwargs. Break it intentionally in demo to show `SyntaxError`. Relate to pytest's `-k` and `--tags` patterns. Show how this scales to custom test runners."),
        (9, "Lambda Expressions", "[ASK] ENGAGEMENT: Ask 'When should you NOT use lambda?' (Complex logic, debugging, PEP-8 compliance). Show how `key=` replaces verbose `def` in test data sorting. Connect to pandas `apply()` and custom pytest markers."),
        (10, "Functional Programming: map() & filter()", "[TIP] AUTOMATION CONTEXT: Log parsing, status normalization, payload sanitization. Emphasize that `map`/`filter` return iterators (memory efficient for large test suites). Live demo: chain them vs list comprehensions."),
        (11, "Functional Programming: reduce() & Comprehensions", "[WARN] REALITY CHECK: `reduce()` is rarely used in modern Python. Show equivalent `sum()` or comprehension. Stress that test frameworks prioritize readability over FP purity. Recommend comprehensions for 90% of data transformations."),
        (12, "Code Modularization", "[GOAL] FRAMEWORK DESIGN: Show how pytest/Playwright organize code. Explain that modularization prevents 'spaghetti test suites'. Demo: move a function to `utils.py`, import it, run. Highlight CI pipeline caching benefits."),
        (13, "The __name__ == '__main__' Guard", "[WARN] CRITICAL FOR AUTOMATION: Demonstrate what happens when you import a script without the guard. Show pytest output vs direct execution. Stress that all framework entry points MUST use this pattern to avoid side effects in CI."),
        (14, "Hands-On Challenge: Flexible Report Generator", "[TIME] TIMING: 15 mins coding, 10 mins review. Provide starter scaffold. Walk through solutions emphasizing defensive `.get()`, type hints, and guard clause for missing config. Relate directly to Allure/pytest-html reporting plugins."),
        (15, "Best Practices & Framework Patterns", "[GOAL] DELIVERY: Summarize as 'The 5 Rules of Framework-Ready Functions'. Show how these practices reduce flaky tests and speed up PR reviews. Recommend `pylint`/`ruff` + `mypy` for automation repos. Open floor for real pain points."),
        (16, "Q&A, Resources & Next Steps", "[ASK] CLOSE: Thank participants. Share QR/code for repo. Ask 'Which concept will you refactor first in your current scripts?' Collect feedback. Preview next session's CI/CD integration focus. End on actionable note.")
    ]

    for slide_num, title, note in notes:
        pdf.add_slide_note(slide_num, title, note)

    filename = "Trainer_Notes_Functions_Advanced.pdf"
    pdf.output(filename)
    print(f"[OK] Successfully generated: {os.path.abspath(filename)}")

if __name__ == "__main__":
    main()