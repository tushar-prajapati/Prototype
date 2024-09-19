import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self.frame, text="Dashboard Overview", font=("Arial", 18, "bold"), bg="#f0f0f0", pady=10)
        header.pack(fill=tk.X)

        self.case_summary_frame = ttk.Frame(self.frame, padding=(10, 5))
        self.case_summary_frame.pack(pady=10, fill=tk.X)
        
        self.create_case_summary("Case 1", "In Progress", 10, "2024-09-18 14:00", "high")
        self.create_case_summary("Case 2", "Completed", 5, "2024-09-17 16:00", "low")
        
        self.alert_frame = ttk.Frame(self.frame, padding=(10, 5))
        self.alert_frame.pack(pady=10, fill=tk.X)
        
        self.create_alert("Critical system alert!", "#d9534f")
        self.create_alert("All systems operational.", "#5bc0de")

        self.resource_frame = ttk.Frame(self.frame, padding=(10, 5))
        self.resource_frame.pack(pady=10, fill=tk.X)
        
        self.create_resource_usage(60, 70) 

    def create_case_summary(self, case_name, status, artifacts, last_activity, priority):
        case_frame = ttk.Frame(self.case_summary_frame, padding=10)
        case_frame.pack(pady=5, fill=tk.X, expand=True)
        
        priority_color = "#d9534f" if priority == "high" else "#5bc0de"
        
        card = ttk.Frame(case_frame, relief="solid", borderwidth=1, padding=10, style="Card.TFrame")
        card.pack(fill=tk.X, expand=True)

        tk.Label(card, text=case_name, font=("Arial", 16, "bold"), anchor='w').pack(fill=tk.X)
        tk.Label(card, text=f"Status: {status}", anchor='w').pack(fill=tk.X)
        tk.Label(card, text=f"Artifacts Found: {artifacts}", anchor='w').pack(fill=tk.X)
        tk.Label(card, text=f"Last Activity: {last_activity}", anchor='w').pack(fill=tk.X)
        tk.Label(card, text=f"Priority: {priority.capitalize()}", foreground=priority_color, anchor='w').pack(fill=tk.X)

    def create_alert(self, message, color):
        alert = tk.Label(self.alert_frame, text=message, bg=color, fg="white", font=("Arial", 12, "bold"), padx=15, pady=10, relief="flat")
        alert.pack(fill=tk.X, pady=5)

    def create_resource_usage(self, cpu_usage, memory_usage):
        usage_frame = ttk.Frame(self.resource_frame)
        usage_frame.pack(pady=5, fill=tk.X)
        
        tk.Label(usage_frame, text="Resource Usage", font=("Arial", 16, "bold")).pack()
        tk.Label(usage_frame, text=f"CPU Usage: {cpu_usage}%", font=("Arial", 14)).pack()
        tk.Label(usage_frame, text=f"Memory Usage: {memory_usage}%", font=("Arial", 14)).pack()

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    dashboard.show()
    root.mainloop()
