import tkinter as tk
from tkinter import messagebox, Tk
from typing import List, Dict, Any, Optional, Callable

def ask_questions_ui(questions: List[Dict[str, Any]], parent: Tk, title: Optional[str] = "Question Input") -> List[str]:
    """
    Display questions one by one in a tkinter UI and collect answers.
    
    Args:
        questions: List of question dictionaries
        title: Window title
        parent: Parent window (important for modal behavior)
    
    Returns:    
        List of answers in the same order as questions
    """
    
    if not questions:
        return []
    
    answers = []
    current_question = [0]
    
    def show_question(q_index):
        if q_index >= len(questions):
            return

            
        # Create window as child of parent if provided
        if parent:
            root = tk.Toplevel(parent)
        else:
            root = tk.Tk()
            
        root.title(title)
        root.geometry("450x250")
        root.configure(bg='lightgray')
        
        # Center the window
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (225)
        y = (root.winfo_screenheight() // 2) - (125)
        root.geometry(f'450x250+{x}+{y}')
        
        question_data = questions[q_index]
        question_text = question_data['question']
        default_value = question_data.get('default', '')
        
        # Progress indicator
        progress_text = f"Question {q_index + 1} of {len(questions)}"
        tk.Label(
            root, 
            text=progress_text,
            font=("Arial", 10),
            bg='lightgray',
            fg='gray'
        ).pack(pady=(10, 5))
        
        # Question label
        tk.Label(
            root,
            text=question_text,
            font=("Arial", 12, "bold"),
            bg='lightgray',
            fg='darkblue',
            wraplength=400
        ).pack(pady=10)
        
        # Show default hint
        if default_value:
            tk.Label(
                root,
                text=f"(Default: {default_value})",
                font=("Arial", 9),
                bg='lightgray',
                fg='gray'
            ).pack(pady=(0, 10))
        
        # Input field
        entry_var = tk.StringVar(value=default_value)
        entry = tk.Entry(
            root,
            textvariable=entry_var,
            font=("Arial", 11),
            width=40,
            relief='sunken',
            bd=2
        )
        entry.pack(pady=10)
        
        def next_question():
            answer = entry_var.get().strip()
            
            if not answer and not default_value:
                messagebox.showerror("Required Field", "Please enter a value for this field.")
                entry.focus()
                return

            if not answer and default_value:
                answer = default_value
                
            answers.append(answer)
            current_question[0] += 1
            root.destroy()  # Use destroy instead of quit+destroy
        
        # Next/Finish button
        tk.Button(
            root,
            text="Next" if q_index < len(questions) - 1 else "Finish",
            command=next_question,
            bg='lightblue',
            font=("Arial", 10, "bold"),
            width=15,
            relief='raised'
        ).pack(pady=20)
        
        # Bind Enter key
        root.bind('<Return>', lambda e: next_question())
        
        # Important: Set focus and grab AFTER window is ready
        root.focus_force()
        entry.focus_set()
        
        # Make modal relative to parent
        if parent:
            root.transient(parent)
            root.grab_set()
        else:
            root.grab_set()
        
        # Wait for window to close
        root.wait_window()
    
    # Show questions one by one
    while current_question[0] < len(questions):
        show_question(current_question[0])
    
    return answers