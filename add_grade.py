from sqlite3 import Connection
from tkinter import Tk
from database import add_grades_db
from get_student_by_roll_no import get_student_by_roll_no
from ui.menu import alert, error_alert
from ui.questions import ask_questions_ui

def add_grade(conn: Connection, parent: Tk) -> None:
    student = get_student_by_roll_no(conn, parent)

    if not student:
        return

    grade_questions = [
        { 'question': 'Enter Assignment Grade (0-100): ', 'default': 0 },
        { 'question': 'Enter Test Grade (0-100): ', 'default': 0 }
    ]

    answers = ask_questions_ui(grade_questions, parent, "Add Grades")

    assignment_grade = int(answers[0]) if answers and answers[0].isdigit() else 0
    test_grade = int(answers[1]) if answers and answers[1].isdigit() else 0

    error = add_grades_db(
        conn,
        student[0],  # roll_number
        [
            ("ASSIGNMENT", assignment_grade),
            ("TEST", test_grade)
        ]
    )

    if error: 
        error_alert("Error", error)
    else:
        alert("Success", f"Grades added for student '{student[1]}' with roll number {student[0]}.")
