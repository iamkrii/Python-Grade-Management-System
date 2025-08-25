import tkinter as tk
from typing import List

def display_text_window(title: str, parent: tk.Tk, lines: List[str]):
    """
    Display a list of strings in a simple scrollable text window.

    Args:
        title: Window title
        lines: List of strings to display (each string is a line)

    Example:
        lines = [
            "📋 All Students Summary",
            "=" * 60,
            "Name            Assignments  Tests    Average  Grade",
            "-" * 60,
    Args:
        title: Window title
        lines: List of strings to display (each string is a line)
    
    Example:
        lines = [
            "📋 All Students Summary",
            "=" * 60,
            "Name            Assignments  Tests    Average  Grade",
            "-" * 60,
            "John Doe        4            2        87.5     B",
            "Jane Smith      3            3        91.2     A"
        ]
        display_text_window("Student Report", lines)
    """
    
    # Create window
    # root = tk.Tk()
    root = tk.Toplevel(parent)
    
    root.title(title)
    root.geometry("600x400")
    root.configure(bg='white')
    
    # Create text widget with scrollbar
    text_frame = tk.Frame(root)
    text_frame.pack(pady=10, padx=20, fill='both', expand=True)
    
    text_widget = tk.Text(
        text_frame,
        font=("Courier", 10),  # Monospace font for alignment
        bg='lightgray',
        fg='black',
        relief='sunken',
        bd=2
    )
    
    scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)
    
    text_widget.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    # Join all lines with newlines and insert
    content = '\n'.join(lines)
    text_widget.insert('1.0', content)
    text_widget.configure(state='disabled')  # Make read-only
    
    # Close button
    close_btn = tk.Button(
        root,
        text="Close",
        command=root.destroy,
        bg='lightblue',
        font=("Arial", 10, "bold"),
        width=10
    )
    close_btn.pack(pady=10)
    
    root.mainloop()