from typing import List
from student import ASSIGNMENT_WEIGHT, TEST_WEIGHT

def calculate_average(grades: List[float]) -> float:
    """Calculate the average of a list of grades"""
    return sum(grades) / len(grades) if grades else 0.0

def calculate_overall(assignments: List[float], tests: List[float]) -> float:
    """Calculate overall average with weights"""
    return (calculate_average(assignments) * ASSIGNMENT_WEIGHT +
            calculate_average(tests) * TEST_WEIGHT)

def get_letter_grade(average: float) -> str:
    """Convert numerical grade to letter grade"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"