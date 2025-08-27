from tkinter import Tk
from get_student_name import get_student_name
from student import StudentDataDict
from ui.menu import alert
from ui.questions import ask_questions_ui

def add_grade(students: StudentDataDict, parent: Tk) -> None:
    """Add a grade for an existing student"""
    name = get_student_name(
        students=students,
        title="Add Student Grade",
        revert_if_no_students=True,
        revert_if_not_found=True,
        parent=parent
    )
    
    if not name:
        return
    
    grade_questions = [
        { 'question': 'Enter Assignment Grade (0-100): ', 'default': 0 },
        { 'question': 'Enter Test Grade (0-100): ', 'default': 0 }
    ]

    answers = ask_questions_ui(grade_questions, parent, "Add Grades")

    assignment_grade = int(answers[0]) if answers and answers[0].isdigit() else 0
    test_grade = int(answers[1]) if answers and answers[1].isdigit() else 0

    students[name]["assignments"].append(assignment_grade)
    students[name]["tests"].append(test_grade)
    
    alert("Success", f"Grades added for student '{name}'.")
