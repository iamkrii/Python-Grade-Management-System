from sqlite3 import Connection
from tkinter import Tk
from database import get_student_report_db
from get_student_by_roll_no import get_student_by_roll_no
from get_student_name import get_student_name
from calculate import calculate_average, calculate_overall, get_letter_grade
from ui.display_data import display_text_window
from ui.menu import error_alert

def view_student_report(conn: Connection, parent: Tk) -> None:
    """Display detailed report for a specific student"""
    student = get_student_by_roll_no(
        conn,
        parent=parent
    )

    if not student:
        return

    data = get_student_report_db(conn, student[0])
    
    if isinstance(data, str):
        error_alert("Error", data)
        return
    
    roll_number = student[0]
    name = student[1]
    
    assignments = []
    tests = []
    for record in data:
        _, _, assessment_type, marks = record
        if assessment_type == 'ASSIGNMENT':
            assignments.append(marks)
        elif assessment_type == 'TEST':
            tests.append(marks)
            
    overall_avg = calculate_overall(assignments, tests)

    display_text_window(
        "Student Report - " + name,
        parent,
        [
            f"\n📊 Report for {name} | Roll No: {roll_number}",
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
