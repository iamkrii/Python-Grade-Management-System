from tkinter import Tk
from database import add_student_db
from ui.menu import alert, error_alert
from get_student_name import get_student_name

from sqlite3 import Connection

def add_student(conn: Connection, parent: Tk) -> None:
    """Add a new student to the system"""

    name = get_student_name(
        title="Add New Student",
        revert_if_found=True,
        parent=parent
    )

    if not name:
        return

    roll_number = add_student_db(conn, name)
    if roll_number:
        alert("Success", f"Student '{name}' added successfully with Roll Number: {roll_number}.")
    else:
        error_alert("Error", f"Failed to add student.")