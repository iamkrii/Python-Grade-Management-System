import tkinter as tk
from tkinter import Tk, messagebox
from typing import Callable

def display_menu_ui(click_command: Callable[[int, Tk], None], on_exit: Callable[[], None]) -> None:
    """
    Displays a modern, styled UI for the Grade Management system menu.
    """
    # --- Window Setup ---
    root = tk.Tk()
    root.title("Grade Management")
    root.geometry("550x785")
    root.resizable(False, False)
    
    # Create gradient background effect using multiple frames
    gradient_bg = "#1a1a2e"
    root.configure(bg=gradient_bg)

    # --- Main Container with Card Design ---
    main_container = tk.Frame(root, bg=gradient_bg)
    main_container.pack(fill="both", expand=True, padx=20, pady=20)
    
    # --- Header Card ---
    header_card = tk.Frame(main_container, bg="#16213e", relief="flat", bd=0)
    header_card.pack(fill="x", pady=(0, 20))
    
    # --- App Icon and Title ---
    title_frame = tk.Frame(header_card, bg="#16213e")
    title_frame.pack(pady=15)
    
    # Large icon
    tk.Label(
        title_frame,
        text="🎓",
        font=("Helvetica", 32),
        bg="#16213e",
        fg="#ffffff"
    ).pack()
    
    # Main title
    tk.Label(
        title_frame,
        text="STUDENT GRADE MANAGEMENT",
        font=("Helvetica", 18, "bold"),
        bg="#16213e",
        fg="#ffffff",
        # letterspace=2
    ).pack()
    
    # Subtitle
    tk.Label(
        title_frame,
        text="Streamline your academic workflow",
        font=("Helvetica", 10),
        bg="#16213e",
        fg="#8892b0"
    ).pack(pady=(5, 0))

    # --- Scrollable Menu Frame ---
    # Create canvas and scrollbar for scrollable menu
    canvas_frame = tk.Frame(main_container, bg="#0f3460")
    canvas_frame.pack(fill="both", expand=True, padx=10)
    
    canvas = tk.Canvas(canvas_frame, bg="#0f3460", highlightthickness=0)
    scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, bg="#1e3a5f", troughcolor="#0f3460")
    scrollable_frame = tk.Frame(canvas, bg="#0f3460")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def resize_scrollable_frame(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_scrollable_frame)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Bind mousewheel and trackpad scrolling to canvas (cross-platform)
    def _on_mousewheel(event):
        if event.num == 4 or event.delta > 0:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            canvas.yview_scroll(1, "units")

    # Windows and MacOS
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    # Linux (X11)
    canvas.bind_all("<Button-4>", _on_mousewheel)
    canvas.bind_all("<Button-5>", _on_mousewheel)

    # --- Menu Options ---
    options = [
        ("➕", "Add New Student", "#4ecdc4"),
        ("📝", "Add Grade for Student", "#45b7d1"),
        ("📊", "View Student Report", "#f9ca24"),
        ("📋", "View All Students", "#6c5ce7"),
        ("🗑️", "Remove Student", "#fd79a8"),
        ("🚪", "Exit", "#74b9ff")
    ]

    # Create buttons with modern card design
    for i, (icon, text, accent_color) in enumerate(options, 1):
        # Button container for hover effect simulation
        btn_container = tk.Frame(
            scrollable_frame, 
            bg="#0f3460"
        )
        btn_container.pack(fill="x", pady=8, padx=8, expand=True)
        
        # Main button frame
        btn_frame = tk.Frame(btn_container, bg="#1e3a5f", relief="flat", bd=0)
        btn_frame.pack(fill="x")
        
        # Left accent bar
        accent_bar = tk.Frame(btn_frame, bg=accent_color, width=4)
        accent_bar.pack(side="left", fill="y")
        accent_bar.pack_propagate(False)
        
        # Button content frame
        content_frame = tk.Frame(btn_frame, bg="#1e3a5f")
        content_frame.pack(side="left", fill="both", expand=True)
        
        # Icon and text container
        text_container = tk.Frame(content_frame, bg="#1e3a5f")
        text_container.pack(fill="x", pady=18, padx=20)
        
        # Icon
        icon_label = tk.Label(
            text_container,
            text=icon,
            font=("Helvetica", 20),
            bg="#1e3a5f",
            fg=accent_color
        )
        icon_label.pack(side="left")
        
        # Option number and text
        text_label = tk.Label(
            text_container,
            text=f"  {i}. {text}",
            font=("Helvetica", 13, "bold"),
            bg="#1e3a5f",
            fg="#ffffff",
            anchor="w"
        )
        text_label.pack(side="left", fill="x", expand=True, padx=(10, 0))
        
        # Make the entire button clickable
        def make_click_handler(option_num):
            return lambda event: click_command(option_num, root)
        
        click_handler = make_click_handler(i)
        
        # Bind click events to all components
        for widget in [btn_frame, content_frame, text_container, icon_label, text_label]:
            widget.bind("<Button-1>", click_handler)
            widget.bind("<Enter>", lambda e, frame=btn_frame, color=accent_color: on_enter(frame, color))
            widget.bind("<Leave>", lambda e, frame=btn_frame: on_leave(frame))
            widget.configure(cursor="hand2")

    # --- Footer ---
    footer_frame = tk.Frame(main_container, bg=gradient_bg)
    footer_frame.pack(fill="x", pady=(20, 0))
    
    tk.Label(
        footer_frame,
        text="💡 Select an option to continue",
        font=("Helvetica", 10),
        bg=gradient_bg,
        fg="#8892b0"
    ).pack()

    # --- Hover Effects ---
    def on_enter(frame, accent_color):
        """Handle mouse enter event for button hover effect"""
        frame.configure(bg="#2a4a6b")
        for child in frame.winfo_children():
            if isinstance(child, tk.Frame):
                child.configure(bg="#2a4a6b")
                for subchild in child.winfo_children():
                    if isinstance(subchild, tk.Frame):
                        subchild.configure(bg="#2a4a6b")
                        for label in subchild.winfo_children():
                            if isinstance(label, tk.Label):
                                label.configure(bg="#2a4a6b")
                    elif isinstance(subchild, tk.Label):
                        subchild.configure(bg="#2a4a6b")

    def on_leave(frame):
        """Handle mouse leave event for button hover effect"""
        frame.configure(bg="#1e3a5f")
        for child in frame.winfo_children():
            if isinstance(child, tk.Frame):
                child.configure(bg="#1e3a5f")
                for subchild in child.winfo_children():
                    if isinstance(subchild, tk.Frame):
                        subchild.configure(bg="#1e3a5f")
                        for label in subchild.winfo_children():
                            if isinstance(label, tk.Label):
                                label.configure(bg="#1e3a5f")
                    elif isinstance(subchild, tk.Label):
                        subchild.configure(bg="#1e3a5f")

    # --- Center window on screen ---
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")

    # handle window close event
    def on_close():
        if yesno_alert("Confirm Exit", "Are you sure you want to exit?"):
            root.destroy()
            on_exit()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # --- Start the Application ---
    root.mainloop()


def alert(title: str, message: str):
    """Display an alert message box."""
    messagebox.showinfo(title, message)

def yesno_alert(title: str, message: str) -> bool:
    """Display a yes/no message box."""
    return messagebox.askyesno(title, message)

def error_alert(title: str, message: str):
    """Display an error message box."""
    messagebox.showerror(title, message)