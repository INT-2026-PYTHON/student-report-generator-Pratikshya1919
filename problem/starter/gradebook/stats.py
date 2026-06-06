"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass

from typing import List, Dict, Set, Tuple

def average_per_student(records: List[Dict]) -> Dict[str, float]:
    """Map each student name to their average score (rounded to 2 decimals)."""
    student_scores = {}
    
    # Group all scores per student
    for record in records:
        name = record["name"]
        score = record["score"]
        if name not in student_scores:
            student_scores[name] = []
        student_scores[name].append(score)
        
    # Calculate averages
    averages = {}
    for name, scores in student_scores.items():
        averages[name] = round(sum(scores) / len(scores), 2)
        
    return averages

def subjects_offered(records: List[Dict]) -> Set[str]:
    """Return the set of unique subjects in the records."""
    # Use a set comprehension to gather unique subjects
    return {record["subject"] for record in records}

def top_scorer(records: List[Dict]) -> Tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    averages = average_per_student(records)
    if not averages:
        return ("", 0.0)
    
    # Find the key with the maximum value
    top_student = max(averages, key=averages.get)
    return (top_student, averages[top_student])

def passing_students(records: List[Dict], threshold: float = 60.0) -> List[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    averages = average_per_student(records)
    
    passing = [name for name, avg in averages.items() if avg >= threshold]
    return sorted(passing)