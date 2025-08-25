from tkinter import Tk
from ui.questions import ask_questions_ui
from ui.menu import alert
from student import StudentDataDict
from typing import Optional

def get_student_name(
  title: str,
  students: StudentDataDict,
  parent: Tk,

  revert_if_no_students: Optional[bool] = False,
  revert_if_not_found: Optional[bool] = False,
  revert_if_found: Optional[bool] = False
) -> str:

  if revert_if_no_students and not students:
    alert("No Students", "No students available! Add students first.")
    return ""

  answer = ask_questions_ui(
    [{'question': "Enter Student Name"}],
    parent,
    title,
  )

  name = answer[0] if answer else ""

  if revert_if_not_found and name not in students:
    alert("Student Not Found", f"Student '{name}' not found!")
    return ""

  if revert_if_found and name in students:
    alert("Student Exists", f"Student '{name}' already exists!")
    return ""

  return name