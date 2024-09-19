import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from evidence_import import EvidenceImport
from analysis import Analysis
from reports import Reports
from help_support import HelpSupport
from dashboard import Dashboard
from ai_ml_analysis import AI_ML_Analysis
from timeline import Timeline

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Triage Tool")
        self.root.geometry("800x600")
        self.root.configure(bg='lightgray')

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.dashboard = Dashboard(self.notebook)
        self.evidence_import = EvidenceImport(self.notebook)
        self.analysis = Analysis(self.notebook)
        self.reports = Reports(self.notebook)
        self.help_support = HelpSupport(self.notebook)
        self.ai_ml_analysis = AI_ML_Analysis(self.notebook)
        self.timeline = Timeline(self.notebook)

        self.notebook.add(self.dashboard.frame, text="Dashboard")
        self.notebook.add(self.evidence_import.frame, text="Evidence Import")
        self.notebook.add(self.analysis.frame, text="Analysis")
        self.notebook.add(self.reports.frame, text="Reports")
        self.notebook.add(self.help_support.frame, text="Help & Support")
        self.notebook.add(self.ai_ml_analysis.frame, text="AI/ML Analysis")
        self.notebook.add(self.timeline.frame, text="Timeline")

        self.notebook.select(self.dashboard.frame)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = MainApp(root)
    root.mainloop()
