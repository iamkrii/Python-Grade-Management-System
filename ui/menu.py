import tkinter as tk
from tkinter import Tk, messagebox
from typing import Callable

def display_menu_ui(click_command: Callable[[int, Tk], None]) -> None:
    """Simplified version that just displays menu and returns choice and root"""
    root = tk.Tk()
    root.title("Grade Management")
    root.geometry("350x300")
    
    tk.Label(root, text="📚 STUDENT GRADE MANAGEMENT 📚", 
             font=("Arial", 11, "bold")).pack(pady=10)
    
    options = [
        "➕ Add New Student",
        "📝 Add Grade for Student", 
        "📊 View Student Report",
        "📋 View All Students",
        "🗑️ Remove Student",
        "🚪 Exit"
    ]
    
    for i, option in enumerate(options, 1):
        tk.Button(
            root,
            text=f"{i}. {option}",
            command=lambda x=i: click_command(x, root),
            width=25,
            pady=5
        ).pack(pady=3)
    
    root.mainloop()

    # Do not destroy root here, return it for further use
    # return root


def alert(title: str, message: str):
    """Display an alert message box."""
    messagebox.showinfo(title, message)

def yesno_alert(title: str, message: str) -> bool:
    """Display a yes/no message box."""
    return messagebox.askyesno(title, message)