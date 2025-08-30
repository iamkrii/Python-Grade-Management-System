from sqlite3 import Connection
from tkinter import Tk
from student import StudentTuple
from ui.questions import ask_questions_ui
from ui.menu import alert, error_alert
from typing import Optional, Union
from database import get_student_by_roll_db

def get_student_by_roll_no(
  conn: Connection,
  parent: Tk,
) -> Union[StudentTuple, None]:

  # if revert_if_no_students and not students:
  #   alert("No Students", "No students available! Add students first.")
  #   return ""

  answer = ask_questions_ui(
    [{'question': "Enter Roll Number"}],
    parent,
    "Get Student by Roll Number",
  )

  roll_number = int(answer[0] if answer else "")

  student = get_student_by_roll_db(conn, roll_number)

  if student:
      return student
  else:
      error_alert("Not Found", f"No student found with Roll Number: {roll_number}.")
