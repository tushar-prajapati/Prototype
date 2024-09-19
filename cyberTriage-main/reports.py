import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
import csv

class Reports:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.frame, text="Comprehensive Reporting Module", font=("Arial", 16))
        label.pack(pady=10)

        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(pady=5, fill=tk.BOTH, expand=True)

        self.summary_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.summary_frame, text="Summary")
        self.create_summary_tab()

        self.findings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.findings_frame, text="Detailed Findings")
        self.create_findings_tab()

        self.recommendations_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.recommendations_frame, text="Recommendations")
        self.create_recommendations_tab()

        self.export_frame = ttk.Frame(self.frame)
        self.export_frame.pack(pady=10, fill=tk.X)

        self.export_button = tk.Button(self.export_frame, text="Export Report", command=self.export_report)
        self.export_button.pack(side=tk.LEFT, padx=5)

        self.export_format = tk.StringVar(value="PDF")
        export_menu = ttk.Combobox(self.export_frame, textvariable=self.export_format, values=["PDF", "JSON", "CSV"])
        export_menu.pack(side=tk.LEFT, padx=5)
        export_menu.bind("<<ComboboxSelected>>", self.update_export_format)

        self.preview_button = tk.Button(self.frame, text="Preview Report", command=self.preview_report)
        self.preview_button.pack(pady=5)

        self.frame.drop_target_register(DND_FILES)
        self.frame.dnd_bind('<<Drop>>', self.on_drop)

    def create_summary_tab(self):
        tk.Label(self.summary_frame, text="Summary Report", font=("Arial", 12)).pack(pady=5)
        self.summary_text = tk.Text(self.summary_frame, wrap=tk.WORD, height=10)
        self.summary_text.pack(pady=5, fill=tk.BOTH, expand=True)

    def create_findings_tab(self):
        tk.Label(self.findings_frame, text="Detailed Findings Report", font=("Arial", 12)).pack(pady=5)
        self.findings_text = tk.Text(self.findings_frame, wrap=tk.WORD, height=10)
        self.findings_text.pack(pady=5, fill=tk.BOTH, expand=True)

    def create_recommendations_tab(self):
     
        tk.Label(self.recommendations_frame, text="Recommendations Report", font=("Arial", 12)).pack(pady=5)
        self.recommendations_text = tk.Text(self.recommendations_frame, wrap=tk.WORD, height=10)
        self.recommendations_text.pack(pady=5, fill=tk.BOTH, expand=True)

    def export_report(self, event=None):
        file_format = self.export_format.get().lower()
        filetypes = {
            "pdf": [("PDF files", "*.pdf")],
            "json": [("JSON files", "*.json")],
            "csv": [("CSV files", "*.csv")]
        }

        file = filedialog.asksaveasfilename(defaultextension=f".{file_format}", filetypes=filetypes[file_format])
        if not file:
            return

        if file_format == "pdf":
            self.save_as_pdf(file)
        elif file_format == "json":
            self.save_as_json(file)
        elif file_format == "csv":
            self.save_as_csv(file)

    def save_as_pdf(self, file):
        c = canvas.Canvas(file, pagesize=letter)
        c.drawString(100, 750, "Summary:")
        c.drawString(100, 730, self.summary_text.get("1.0", tk.END))
        c.drawString(100, 680, "Detailed Findings:")
        c.drawString(100, 660, self.findings_text.get("1.0", tk.END))
        c.drawString(100, 610, "Recommendations:")
        c.drawString(100, 590, self.recommendations_text.get("1.0", tk.END))
        c.save()

    def save_as_json(self, file):
        report = {
            "summary": self.summary_text.get("1.0", tk.END).strip(),
            "findings": self.findings_text.get("1.0", tk.END).strip(),
            "recommendations": self.recommendations_text.get("1.0", tk.END).strip()
        }
        with open(file, 'w') as f:
            json.dump(report, f, indent=4)

    def save_as_csv(self, file):
        report = [
            ["Section", "Content"],
            ["Summary", self.summary_text.get("1.0", tk.END).strip()],
            ["Detailed Findings", self.findings_text.get("1.0", tk.END).strip()],
            ["Recommendations", self.recommendations_text.get("1.0", tk.END).strip()]
        ]
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(report)

    def preview_report(self):
        summary = self.summary_text.get("1.0", tk.END).strip()
        findings = self.findings_text.get("1.0", tk.END).strip()
        recommendations = self.recommendations_text.get("1.0", tk.END).strip()

        preview_text = (f"Summary:\n{summary}\n\n"
                        f"Detailed Findings:\n{findings}\n\n"
                        f"Recommendations:\n{recommendations}")

        messagebox.showinfo("Report Preview", preview_text)

    def update_export_format(self, event=None):
        pass

    def on_drop(self, event):
        files = event.data.split()
        if files:
            file_path = files[0]
            messagebox.showinfo("File Dropped", f"Dropped file: {file_path}")

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = TkinterDnD.Tk() 
    reports = Reports(root)
    reports.show()
    root.mainloop()
