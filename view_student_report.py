from tkinter import Tk
from student import StudentDataDict
from get_student_name import get_student_name
from calculate import calculate_average, calculate_overall, get_letter_grade
from ui.display_data import display_text_window

def view_student_report(students: StudentDataDict, parent: Tk) -> None:
    """Display detailed report for a specific student"""
    name = get_student_name(
        students=students,
        title="View Student Report",
        revert_if_no_students=True,
        revert_if_not_found=True,
        parent=parent
    )
    
    if not name:
        return

    data = students[name]
    assignments = data["assignments"]
    tests = data["tests"]
    overall_avg = calculate_overall(assignments, tests)

    display_text_window(
        "Student Report - " + name,
        parent,
        [
            f"\n📊 Report for {name}",
            "-" * 30,
            f"Assignment Grades: {assignments}",
            f"Assignment Average: {calculate_average(assignments):.1f}",
            f"Test Grades: {tests}",
            f"Test Average: {calculate_average(tests):.1f}",
            "-" * 30,
            f"Overall Average: {overall_avg:.1f}",
            f"Letter Grade: {get_letter_grade(overall_avg)}",
            f"Total Assignments: {len(assignments)}",
            f"Total Tests: {len(tests)}",
        ],
    )
