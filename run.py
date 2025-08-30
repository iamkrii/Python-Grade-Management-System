import sys
from tkinter import Tk

from add_student import add_student
from add_grade import add_grade
from view_student_report import view_student_report
from view_all_students import view_all_students
from remove_student import remove_student
from ui.menu import display_menu_ui

from database import initialize_database

def main() -> None:
    """Main function that runs the program"""
    print("Welcome to the Student Grade Management System!")

    # Initialize the database
    conn = initialize_database()

    if conn is None:
        print("Failed to initialize database.")
        sys.exit(1)

    menu_actions = {
        1: add_student,
        2: add_grade,
        3: view_student_report,
        4: view_all_students,
        5: remove_student,
    }

    def handle_choice(choice: int, root: Tk):
        if choice == 6:
            conn.close()
            root.quit()
            root.destroy()
            sys.exit(0)

        action = menu_actions.get(choice)
        if action:
            action(conn, root)

    def on_window_close():
        conn.close()
        sys.exit(0)
            # root.deiconify()  # ✅ Show menu again
            
    display_menu_ui(handle_choice)



if __name__ == "__main__":
    main()