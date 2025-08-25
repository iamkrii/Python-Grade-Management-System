from tkinter import Tk
from student import StudentDataDict
from ui.menu import alert
from get_student_name import get_student_name

def add_student(students: StudentDataDict, parent: Tk) -> None:
    """Add a new student to the system"""

    name = get_student_name(
        students=students,
        title="Add New Student",
        revert_if_found=True,
        parent=parent
    )

    if not name:
        return

    students[name] = {"assignments": [], "tests": []}
    alert("Success", f"Student '{name}' added successfully!")