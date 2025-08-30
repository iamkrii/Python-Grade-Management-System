from sqlite3 import Connection
from tkinter import Tk
from database import get_all_students_db, get_total_students_count_db
from calculate import calculate_overall, get_letter_grade
from ui.display_data import display_text_window
from ui.menu import error_alert

def view_all_students(conn: Connection, parent: Tk) -> None:
    """Display summary for all students"""
    count = get_total_students_count_db(conn)
    
    if isinstance(count, str):
        error_alert("Error", "No students found.")
        return

    data_to_display = [
        "📋 All Students Summary",
        "=" * 70,
        f"{'Name':<15} {'Roll No.':<10} {'Assignments':<12} {'Tests':<8} {'Average':<8} {'Grade':<5}",
        "-" * 70
    ]
    
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
        data_to_display.append(f"{data['name']:<15} {roll_number:<10} {len(data['assignments']):<12} {len(data['tests']):<8} {overall_avg:<8.1f} {letter:<5}")

    display_text_window("All Students Summary", parent, data_to_display)