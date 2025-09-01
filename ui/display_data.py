
import tkinter as tk
from tkinter import ttk
from typing import List

from ui.menu import alert

def display_tabular_window(title: str, parent: tk.Tk, headers: List[str], rows: List[List[str]], icon: str = "📊", info_text: str = ""):
    """
    Displays a beautiful tabular data window with modern styling.
    
    Args:
        title: Window title
        parent: Parent window
        headers: List of column headers
        rows: List of rows, where each row is a list of column values
        icon: Icon to display in header (optional)
        info_text: Additional information to display above the table (optional)
    """
    # Create window
    root = tk.Toplevel(parent)
    
    root.title(title)
    root.geometry("800x600")
    root.resizable(True, True)
    root.minsize(600, 400)
    
    # Modern gradient background
    gradient_bg = "#1a1a2e"
    root.configure(bg=gradient_bg)
    
    # --- Main Container ---
    main_container = tk.Frame(root, bg=gradient_bg)
    main_container.pack(fill="both", expand=True, padx=25, pady=20)
    
    # --- Header Section ---
    header_frame = tk.Frame(main_container, bg="#16213e", relief="flat", bd=0)
    header_frame.pack(fill="x", pady=(0, 15))
    
    # Title with icon
    title_container = tk.Frame(header_frame, bg="#16213e")
    title_container.pack(pady=12)
    
    # Document icon
    tk.Label(
        title_container,
        text=icon,
        font=("Helvetica", 20),
        bg="#16213e",
        fg="#ffffff"
    ).pack()
    
    # Window title
    tk.Label(
        title_container,
        text=title,
        font=("Helvetica", 16, "bold"),
        bg="#16213e",
        fg="#ffffff"
    ).pack(pady=(5, 0))
    
    # Record count
    tk.Label(
        title_container,
        text=f"{len(rows)} record(s) found",
        font=("Helvetica", 9),
        bg="#16213e",
        fg="#8892b0"
    ).pack(pady=(3, 0))
    
    # --- Table Card ---
    table_card = tk.Frame(main_container, bg="#0f3460", relief="flat", bd=0)
    table_card.pack(fill="both", expand=True, pady=(0, 15))
    
    # Table header
    table_header = tk.Frame(table_card, bg="#1e3a5f")
    table_header.pack(fill="x", padx=2, pady=2)
    
    tk.Label(
        table_header,
        text="📊 Data Table",
        font=("Helvetica", 11, "bold"),
        bg="#1e3a5f",
        fg="#4ecdc4",
        anchor="w"
    ).pack(side="left", padx=15, pady=6)
    
    # --- Treeview Container ---
    tree_container = tk.Frame(table_card, bg="#2c3e50")
    tree_container.pack(fill="both", expand=True, padx=2, pady=(0, 2))
    
    # Configure ttk styles for modern appearance
    style = ttk.Style()
    
    # Configure Treeview style
    style.theme_use('clam')
    style.configure("Custom.Treeview",
                   background="#2c3e50",
                   foreground="#ecf0f1",
                   fieldbackground="#2c3e50",
                   borderwidth=0,
                   font=("Consolas", 10))
    
    style.configure("Custom.Treeview.Heading",
                   background="#34495e",
                   foreground="#ffffff",
                   borderwidth=1,
                   relief="flat",
                   font=("Helvetica", 11, "bold"))
    
    # Configure selection colors
    style.map("Custom.Treeview",
             background=[('selected', '#3498db')],
             foreground=[('selected', '#ffffff')])
    
    style.map("Custom.Treeview.Heading",
             background=[('active', '#4ecdc4')],
             foreground=[('active', '#2c3e50')])
    
    # Create Treeview
    tree = ttk.Treeview(tree_container, columns=headers, show='headings', style="Custom.Treeview")
    
    # Configure column headings
    for header in headers:
        tree.heading(header, text=header, anchor="center")
        tree.column(header, anchor="center", minwidth=80, width=120)
    
    # Insert data rows
    for i, row in enumerate(rows):
        # Alternate row colors for better readability
        tags = ('evenrow',) if i % 2 == 0 else ('oddrow',)
        tree.insert('', 'end', values=row, tags=tags)
    
    # Configure row colors
    tree.tag_configure('evenrow', background='#34495e', foreground='#ecf0f1')
    tree.tag_configure('oddrow', background='#2c3e50', foreground='#ecf0f1')
    
    # Custom scrollbar for table
    tree_scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=tree_scrollbar.set)
    
    # Horizontal scrollbar
    h_scrollbar = ttk.Scrollbar(tree_container, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=h_scrollbar.set)
    
    # Pack table and scrollbars
    tree.grid(row=0, column=0, sticky="nsew")
    tree_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")
    
    # Configure grid weights
    tree_container.grid_rowconfigure(0, weight=1)
    tree_container.grid_columnconfigure(0, weight=1)
    
    # --- Action Bar ---
    action_bar = tk.Frame(main_container, bg=gradient_bg)
    action_bar.pack(fill="x", pady=(0, 5))
    
    # Statistics info
    stats_frame = tk.Frame(action_bar, bg=gradient_bg)
    stats_frame.pack(side="left")
    
    tk.Label(
        stats_frame,
        text="💡 Double-click rows to select • Use arrow keys to navigate",
        font=("Helvetica", 9),
        bg=gradient_bg,
        fg="#8892b0"
    ).pack()
    
    # --- Button Container ---
    button_container = tk.Frame(action_bar, bg=gradient_bg)
    button_container.pack(side="right")
    
    # Close button with modern styling
    close_btn = tk.Frame(button_container, bg="#e74c3c", relief="flat", bd=0)
    close_btn.pack(side="right")
    
    close_content = tk.Frame(close_btn, bg="#e74c3c")
    close_content.pack(padx=2, pady=2)
    
    close_label = tk.Label(
        close_content,
        text="✕ Close",
        font=("Helvetica", 10, "bold"),
        bg="#e74c3c",
        fg="#ffffff",
        cursor="hand2",
        padx=15,
        pady=6
    )
    close_label.pack()
    
    # Close button hover effects
    def on_close_enter(event):
        close_btn.configure(bg="#c0392b")
        close_content.configure(bg="#c0392b")
        close_label.configure(bg="#c0392b")
    
    def on_close_leave(event):
        close_btn.configure(bg="#e74c3c")
        close_content.configure(bg="#e74c3c")
        close_label.configure(bg="#e74c3c")
    
    # Bind events to close button
    for widget in [close_btn, close_content, close_label]:
        widget.bind("<Button-1>", lambda e: root.destroy())
        widget.bind("<Enter>", on_close_enter)
        widget.bind("<Leave>", on_close_leave)
    
    # --- Keyboard Shortcuts ---
    root.bind('<Escape>', lambda e: root.destroy())
    root.bind('<Control-w>', lambda e: root.destroy())
    
    # --- Center window on screen ---
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Focus the window
    root.focus_set()
    root.grab_set()  # Make window modal
    
    root.mainloop()