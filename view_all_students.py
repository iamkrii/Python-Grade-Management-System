from tkinter import Tk
from student import StudentDataDict
from calculate import calculate_overall, get_letter_grade
from ui.display_data import display_text_window
from ui.menu import alert

def view_all_students(students: StudentDataDict, parent: Tk) -> None:
    """Display summary for all students"""
    if not students:
        alert("No Students", "No students available! Add students first.")
        return

    data_to_display = [
        "📋 All Students Summary",
        "=" * 60,
        f"{'Name':<15} {'Assignments':<12} {'Tests':<8} {'Average':<8} {'Grade':<5}",
        "-" * 60
    ]

    for name, data in students.items():
        overall_avg = calculate_overall(data["assignments"], data["tests"])
        letter = get_letter_grade(overall_avg)
        data_to_display.append(f"{name:<15} {len(data['assignments']):<12} {len(data['tests']):<8} {overall_avg:<8.1f} {letter:<5}")

    display_text_window("All Students Summary", parent, data_to_display)