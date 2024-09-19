import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import os

class HelpSupport:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):

        label = tk.Label(self.frame, text="Help and Support", font=("Arial", 16))
        label.pack(pady=10)

        icon_path = "path/to/help_icon.png" 
        if os.path.exists(icon_path):
            self.help_icon = tk.PhotoImage(file=icon_path)
            help_button = tk.Button(self.frame, image=self.help_icon, command=self.show_help)
            help_button.pack(side=tk.RIGHT, padx=10, pady=10)
        else:
            print(f"Error: The file {icon_path} does not exist.")
            help_button = tk.Button(self.frame, text="Help", command=self.show_help)
            help_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(pady=5, fill=tk.BOTH, expand=True)

        self.tutorial_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.tutorial_frame, text="Guided Tutorials")
        self.create_tutorial_tab()

        self.knowledge_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.knowledge_frame, text="Knowledge Base")
        self.create_knowledge_tab()

        self.support_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.support_frame, text="Support Contact")
        self.create_support_tab()

    def create_tutorial_tab(self):
        tk.Label(self.tutorial_frame, text="Interactive Tutorials and Videos", font=("Arial", 12)).pack(pady=5)
        self.tutorial_text = ScrolledText(self.tutorial_frame, wrap=tk.WORD, height=15)
        self.tutorial_text.pack(pady=5, fill=tk.BOTH, expand=True)
        self.tutorial_text.insert(tk.END, "Tutorials and videos for each module will be available here.")

    def create_knowledge_tab(self):
        tk.Label(self.knowledge_frame, text="Searchable Knowledge Base", font=("Arial", 12)).pack(pady=5)
        
        self.search_frame = ttk.Frame(self.knowledge_frame)
        self.search_frame.pack(pady=5, fill=tk.X)

        tk.Label(self.search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_knowledge_base)
        self.search_button.pack(side=tk.RIGHT, padx=5)

        self.knowledge_text = ScrolledText(self.knowledge_frame, wrap=tk.WORD, height=15)
        self.knowledge_text.pack(pady=5, fill=tk.BOTH, expand=True)
        self.knowledge_text.insert(tk.END, "FAQ, troubleshooting tips, and best practices will be available here.")

    def create_support_tab(self):
        tk.Label(self.support_frame, text="Support Contact Options", font=("Arial", 12)).pack(pady=5)
        
        self.support_text = tk.Text(self.support_frame, wrap=tk.WORD, height=10)
        self.support_text.pack(pady=5, fill=tk.BOTH, expand=True)
        self.support_text.insert(tk.END, "For support, please contact us via:\n"
                                          "Email: support@example.com\n"
                                          "Phone: +123-456-7890\n"
                                          "Live Chat: Available on our website")

    def show_help(self):
        messagebox.showinfo("Help", "Help documentation and tutorials will be provided here.")

    def search_knowledge_base(self):
        search_query = self.search_entry.get()
        messagebox.showinfo("Search", f"Searching for: {search_query}")

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk() 
    help_support = HelpSupport(root)
    help_support.show()
    root.mainloop()
