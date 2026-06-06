"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass


from typing import List, Dict
# Relative import from the stats module in the same package folder
from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def format_report(records: List[Dict]) -> str:
    """
    Build a human-readable, multi-line report using the functions in stats.py.
    """
    # 1. Fetch data evaluations from stats module
    total_records = len(records)
    subjects = sorted(list(subjects_offered(records)))
    averages = average_per_student(records)
    top_name, top_score = top_scorer(records)
    passers = passing_students(records, threshold=60.0)
    
    # 2. Start constructing the multi-line string
    lines = [
        "=== Gradebook Report ===",
        f"Total records: {total_records}",
        f"Subjects offered: {', '.join(subjects)}",
        "",
        "Averages:"
    ]
    
    # List student averages sorted alphabetically by their name
    for student in sorted(averages.keys()):
        lines.append(f"  {student:<8} : {averages[student]}")
        
    lines.append("")
    lines.append(f"Top scorer: {top_name} ({top_score})")
    lines.append(f"Passing students (>= 60.0): {', '.join(passers)}")
    
    # Connect all elements cleanly with newlines
    return "\n".join(lines)