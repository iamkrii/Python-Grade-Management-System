from tkinter import Tk
from student import StudentDataDict
from ui.menu import alert, yesno_alert
from get_student_name import get_student_name

def remove_student(students: StudentDataDict, parent: Tk) -> None:
    """Remove a student from the system"""
    name = get_student_name(
        students=students,
        title="Remove Student",
        revert_if_no_students=True,
        revert_if_not_found=True,
        parent=parent
    )
    
    if not name:
        return

    if yesno_alert("Remove Student", f"Are you sure you want to remove '{name}'?"):
        del students[name]
        alert("Success", f"✅ Student '{name}' removed successfully!")
    else:
        return