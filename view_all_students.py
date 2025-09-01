from sqlite3 import Connection
from tkinter import Tk
from database import get_all_students_db, get_total_students_count_db
from calculate import calculate_overall, get_letter_grade
from ui.display_data import display_tabular_window
from ui.menu import error_alert

def view_all_students(conn: Connection, parent: Tk) -> None:
    """Display summary for all students"""
    count = get_total_students_count_db(conn)
    
    if isinstance(count, str):
        error_alert("Error", "No students found.")
        return

    headers = [
        'Name',
        'Roll No.',
        'Assignments',
        'Tests',
        'Average',
        'Grade'
    ]
    
    data_to_display = []
    
    data = get_all_students_db(conn)

    students = {}
    for record in data:
        roll_number, student_name, assessment_type, marks = record
        if roll_number not in students:
            students[roll_number] = {
                "name": student_name,
                "assignments": [],
                "tests": []
            }
        if assessment_type == "assignment":
            students[roll_number]["assignments"].append(marks)
        elif assessment_type == "test":
            students[roll_number]["tests"].append(marks)

    for roll_number, data in students.items():
        overall_avg = calculate_overall(data["assignments"], data["tests"])
        letter = get_letter_grade(overall_avg)
        data_to_display.append([
            data['name'],
            roll_number,
            len(data['assignments']),
            len(data['tests']),
            overall_avg,
            letter
        ])

    display_tabular_window("All Students Summary", parent, headers, data_to_display, info_text=f"Total Students: {count}")