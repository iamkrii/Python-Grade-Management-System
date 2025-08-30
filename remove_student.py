from sqlite3 import Connection
from tkinter import Tk
from database import remove_student_db
from get_student_by_roll_no import get_student_by_roll_no
from ui.menu import alert, error_alert, yesno_alert

def remove_student(conn: Connection, parent: Tk) -> None:
    """Remove a student from the system"""
    student = get_student_by_roll_no(conn, parent)

    if not student:
        return

    if yesno_alert("Remove Student", f"Are you sure you want to remove '{student[1]}'?"):
        err = remove_student_db(conn, student[0])
        if err:
            error_alert("Error", err)
        else:
            alert("Success", f"✅ Student '{student[1]}' removed successfully!")
    else:
        return