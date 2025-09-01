import tkinter as tk
from tkinter import messagebox, Tk
from typing import List, Dict, Any, Optional

def ask_questions_ui(questions: List[Dict[str, Any]], parent: Tk, title: Optional[str] = "Question Input") -> List[str]:
    """
    Display questions one by one in a beautiful modern UI and collect answers.
    
    Args:
        questions: List of question dictionaries with 'question' key and optional 'default' key
        parent: Parent window (important for modal behavior)
        title: Window title
    
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

        # Create window as child of parent
        if parent:
            root = tk.Toplevel(parent)
        else:
            root = tk.Tk()
            
        root.title(title)
        root.geometry("550x400")
        root.resizable(False, False)
        
        # Modern gradient background
        gradient_bg = "#1a1a2e"
        root.configure(bg=gradient_bg)
        
        # --- Main Container ---
        main_container = tk.Frame(root, bg=gradient_bg)
        main_container.pack(fill="both", expand=True, padx=25, pady=20)
        
        # --- Header Card ---
        header_card = tk.Frame(main_container, bg="#16213e", relief="flat", bd=0)
        header_card.pack(fill="x", pady=(0, 20))
        
        header_content = tk.Frame(header_card, bg="#16213e")
        header_content.pack(pady=15)
        
        # Question icon
        tk.Label(
            header_content,
            text="❓",
            font=("Helvetica", 24),
            bg="#16213e",
            fg="#f39c12"
        ).pack()
        
        if title:
            # Window title
            tk.Label(
                header_content,
                text=title,
                font=("Helvetica", 14, "bold"),
                bg="#16213e",
                fg="#ffffff"
            ).pack(pady=(5, 0))
        
        # Progress indicator with modern styling
        progress_frame = tk.Frame(header_card, bg="#16213e")
        progress_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        # Progress bar background
        progress_bg = tk.Frame(progress_frame, bg="#0f3460", height=6)
        progress_bg.pack(fill="x", pady=5)
        progress_bg.pack_propagate(False)
        
        # Progress bar fill
        progress_percent = (q_index + 1) / len(questions)
        progress_fill = tk.Frame(progress_bg, bg="#4ecdc4", height=6)
        progress_fill.place(x=0, y=0, relwidth=progress_percent, height=6)
        
        # Progress text
        progress_text = f"Question {q_index + 1} of {len(questions)}"
        tk.Label(
            progress_frame,
            text=progress_text,
            font=("Helvetica", 9),
            bg="#16213e",
            fg="#8892b0"
        ).pack()
        
        # --- Question Card ---
        question_card = tk.Frame(main_container, bg="#0f3460", relief="flat", bd=0)
        question_card.pack(fill="both", expand=True, pady=(0, 20))
        
        # Question header
        q_header = tk.Frame(question_card, bg="#1e3a5f")
        q_header.pack(fill="x", padx=2, pady=2)
        
        tk.Label(
            q_header,
            text="💬 Please Answer",
            font=("Helvetica", 11, "bold"),
            bg="#1e3a5f",
            fg="#45b7d1",
            anchor="w"
        ).pack(side="left", padx=15, pady=8)
        
        # Question content area
        question_content = tk.Frame(question_card, bg="#2c3e50")
        question_content.pack(fill="both", expand=True, padx=2, pady=(0, 2))
        
        question_data = questions[q_index]
        question_text = question_data['question']
        default_value = question_data.get('default', '')
        
        # Question text with better styling
        question_label = tk.Label(
            question_content,
            text=question_text,
            font=("Helvetica", 12),
            bg="#2c3e50",
            fg="#ecf0f1",
            wraplength=480,
            justify="left",
            anchor="w"
        )
        question_label.pack(pady=20, padx=20, anchor="w")
        
        # Default value hint
        if default_value:
            hint_frame = tk.Frame(question_content, bg="#34495e")
            hint_frame.pack(fill="x", padx=20, pady=(0, 15))
            
            tk.Label(
                hint_frame,
                text=f"💡 Default: {default_value}",
                font=("Helvetica", 9),
                bg="#34495e",
                fg="#f39c12",
                anchor="w"
            ).pack(padx=10, pady=5, anchor="w")
        
        # Input field with modern styling
        input_frame = tk.Frame(question_content, bg="#2c3e50")
        input_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        entry_var = tk.StringVar(value=default_value)
        entry = tk.Entry(
            input_frame,
            textvariable=entry_var,
            font=("Helvetica", 12),
            bg="#34495e",
            fg="#ecf0f1",
            relief="flat",
            bd=0,
            insertbackground="#4ecdc4",
            selectbackground="#3498db",
            selectforeground="#ffffff"
        )
        entry.pack(fill="x", ipady=8, ipadx=10)
        
        # Input field focus styling
        def on_entry_focus_in(event):
            entry.configure(bg="#3d566e")
        
        def on_entry_focus_out(event):
            entry.configure(bg="#34495e")
        
        entry.bind("<FocusIn>", on_entry_focus_in)
        entry.bind("<FocusOut>", on_entry_focus_out)
        
        # --- Action Buttons ---
        button_frame = tk.Frame(main_container, bg=gradient_bg)
        button_frame.pack(fill="x")
        
        # Skip button (for optional questions)
        if default_value:  # Only show skip if there's a default
            skip_btn = tk.Frame(button_frame, bg="#95a5a6", relief="flat", bd=0)
            skip_btn.pack(side="left")
            
            skip_content = tk.Frame(skip_btn, bg="#95a5a6")
            skip_content.pack(padx=2, pady=2)
            
            skip_label = tk.Label(
                skip_content,
                text="⏭️ Skip",
                font=("Helvetica", 10, "bold"),
                bg="#95a5a6",
                fg="#ffffff",
                cursor="hand2",
                padx=15,
                pady=8
            )
            skip_label.pack()
            
            def on_skip_enter(event):
                skip_btn.configure(bg="#7f8c8d")
                skip_content.configure(bg="#7f8c8d")
                skip_label.configure(bg="#7f8c8d")
            
            def on_skip_leave(event):
                skip_btn.configure(bg="#95a5a6")
                skip_content.configure(bg="#95a5a6")
                skip_label.configure(bg="#95a5a6")
            
            def skip_question(event=None):
                answers.append(default_value)
                current_question[0] += 1
                root.destroy()
            
            for widget in [skip_btn, skip_content, skip_label]:
                widget.bind("<Button-1>", skip_question)
                widget.bind("<Enter>", on_skip_enter)
                widget.bind("<Leave>", on_skip_leave)
        
        # Next/Finish button
        next_btn = tk.Frame(button_frame, bg="#27ae60", relief="flat", bd=0)
        next_btn.pack(side="right")
        
        next_content = tk.Frame(next_btn, bg="#27ae60")
        next_content.pack(padx=2, pady=2)
        
        button_text = "✓ Finish" if q_index == len(questions) - 1 else "→ Next"
        next_label = tk.Label(
            next_content,
            text=button_text,
            font=("Helvetica", 10, "bold"),
            bg="#27ae60",
            fg="#ffffff",
            cursor="hand2",
            padx=20,
            pady=8
        )
        next_label.pack()
        
        def on_next_enter(event):
            next_btn.configure(bg="#219a52")
            next_content.configure(bg="#219a52")
            next_label.configure(bg="#219a52")
        
        def on_next_leave(event):
            next_btn.configure(bg="#27ae60")
            next_content.configure(bg="#27ae60")
            next_label.configure(bg="#27ae60")
        
        def next_question(event=None):
            answer = entry_var.get().strip()
            
            # Validation
            if not answer and not default_value:
                messagebox.showerror("Required Field", "Please enter a value for this field.")
                entry.focus()
                return
            
            if not answer and default_value:
                answer = default_value
                
            answers.append(answer)
            current_question[0] += 1
            root.destroy()
        
        # Bind events to next button
        for widget in [next_btn, next_content, next_label]:
            widget.bind("<Button-1>", next_question)
            widget.bind("<Enter>", on_next_enter)
            widget.bind("<Leave>", on_next_leave)
        
        # Keyboard shortcuts
        root.bind('<Return>', next_question)
        root.bind('<Escape>', lambda e: root.destroy())
        
        # Set focus and make modal
        root.focus_force()
        entry.focus_set()
        if parent:
            root.transient(parent)
            root.grab_set()
        
        # Wait for this window to close before continuing
        root.wait_window()
    
    # Show questions one by one
    while current_question[0] < len(questions):
        show_question(current_question[0])
    
    return answers