import sys
from tkinter import Tk
from student import StudentDataDict

from add_student import add_student
from add_grade import add_grade
from view_student_report import view_student_report
from view_all_students import view_all_students
from remove_student import remove_student
from ui.menu import display_menu_ui

# Dictionary to store all student data
# Structure: {student_name: {"assignments": [grades], "tests": [grades]}}
students: StudentDataDict = {}

def main() -> None:
    """Main function that runs the program"""
    print("Welcome to the Student Grade Management System!")

    menu_actions = {
        1: add_student,
        2: add_grade,
        3: view_student_report,
        4: view_all_students,
        5: remove_student,
    }

    def handle_choice(choice: int, root: Tk):
        if choice == 6:
            root.quit()
            root.destroy()
            sys.exit(0) 

        action = menu_actions.get(choice)
        if action:
            # root.withdraw()  # ✅ Hide menu while action runs
            action(students, root)
            # root.deiconify()  # ✅ Show menu again
            
    display_menu_ui(handle_choice)



if __name__ == "__main__":
    main()