import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class Analysis:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
      
        label = tk.Label(self.frame, text="Automated Analysis Dashboard", font=("Arial", 16))
        label.pack(pady=10)

        self.tab_control = ttk.Notebook(self.frame)
        self.file_analysis_tab = ttk.Frame(self.tab_control)
        self.network_analysis_tab = ttk.Frame(self.tab_control)
        self.log_analysis_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.file_analysis_tab, text="File Analysis")
        self.tab_control.add(self.network_analysis_tab, text="Network Analysis")
        self.tab_control.add(self.log_analysis_tab, text="Log Analysis")
        self.tab_control.pack(expand=1, fill="both")

        self.filter_panel = ttk.Frame(self.frame)
        self.filter_panel.pack(side=tk.LEFT, padx=10, fill=tk.Y)

        self.filter_label = tk.Label(self.filter_panel, text="Filters", font=("Arial", 12))
        self.filter_label.pack(pady=5)

        self.file_type_label = tk.Label(self.filter_panel, text="File Type")
        self.file_type_label.pack(pady=5)
        self.file_type_combo = ttk.Combobox(self.filter_panel, values=["All", "Documents", "Images", "Logs", "Network"])
        self.file_type_combo.pack(pady=5)

        self.date_label = tk.Label(self.filter_panel, text="Date")
        self.date_label.pack(pady=5)
        self.date_entry = tk.Entry(self.filter_panel)
        self.date_entry.pack(pady=5)

        self.search_button = tk.Button(self.filter_panel, text="Search", command=self.search)
        self.search_button.pack(pady=10)

        self.canvas = Canvas(self.frame)
        self.canvas.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True)
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.plot_data()

        self.progress_frame = ttk.Frame(self.frame)
        self.progress_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.progress_label = tk.Label(self.progress_frame, text="Analysis Progress:", font=("Arial", 12))
        self.progress_label.pack(side=tk.LEFT)

        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(side=tk.LEFT)

        self.update_progress()

        self.anomaly_label = tk.Label(self.frame, text="Anomalies Highlighted Below:", font=("Arial", 12))
        self.anomaly_label.pack(pady=10)

        self.anomaly_listbox = tk.Listbox(self.frame)
        self.anomaly_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.highlight_anomalies()

    def plot_data(self):
        sizes = [15, 30, 45, 10]
        labels = ["Files", "Logs", "Network Traffic", "Others"]
        self.ax.clear()
        self.ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        self.ax.axis('equal')  

        self.canvas_figure = FigureCanvasTkAgg(self.fig, master=self.canvas)
        self.canvas_figure.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas_figure.draw()

    def search(self):

        file_type = self.file_type_combo.get()
        date = self.date_entry.get()
        print(f"Searching for files of type '{file_type}' and date '{date}'")

    def update_progress(self):
        self.progress_bar["value"] = random.randint(0, 100)
        self.frame.after(1000, self.update_progress)  

    def highlight_anomalies(self):
        anomalies = ["Anomaly 1: Suspicious file type", "Anomaly 2: High network traffic"]
        for anomaly in anomalies:
            self.anomaly_listbox.insert(tk.END, anomaly)

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
