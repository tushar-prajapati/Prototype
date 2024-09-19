import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Timeline:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.frame, text="Interactive Timeline and Graphical Summaries", font=("Arial", 16))
        label.pack(pady=10)

        filter_frame = ttk.Frame(self.frame)
        filter_frame.pack(pady=5, fill=tk.X)

        self.filter_type = tk.StringVar(value="all")
        type_label = tk.Label(filter_frame, text="Filter by Type:")
        type_label.pack(side=tk.LEFT, padx=5)
        type_menu = ttk.Combobox(filter_frame, textvariable=self.filter_type, values=["all", "normal", "suspicious"])
        type_menu.pack(side=tk.LEFT, padx=5)
        type_menu.bind("<<ComboboxSelected>>", self.update_timeline)

        self.filter_date = tk.StringVar(value="")
        date_label = tk.Label(filter_frame, text="Filter by Date (YYYY-MM-DD):")
        date_label.pack(side=tk.LEFT, padx=5)
        date_entry = ttk.Entry(filter_frame, textvariable=self.filter_date)
        date_entry.pack(side=tk.LEFT, padx=5)
        date_entry.bind("<Return>", self.update_timeline)

        self.timeline_canvas = tk.Canvas(self.frame, bg='white', height=200)
        self.timeline_canvas.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient='horizontal', command=self.timeline_canvas.xview)
        self.scrollbar.pack(fill=tk.X, side=tk.BOTTOM)
        self.timeline_canvas.configure(xscrollcommand=self.scrollbar.set)

        self.events = [
            {"time": "2024-09-01 10:00", "event": "System Boot", "type": "normal"},
            {"time": "2024-09-01 10:15", "event": "File Access", "type": "normal"},
            {"time": "2024-09-01 10:30", "event": "Network Connection", "type": "suspicious"}
        ]

        self.event_ids = []
        self.draw_timeline()

        self.timeline_canvas.bind("<Button-1>", self.on_canvas_click)

        zoom_frame = ttk.Frame(self.frame)
        zoom_frame.pack(pady=5, fill=tk.X)
        zoom_label = tk.Label(zoom_frame, text="Zoom:")
        zoom_label.pack(side=tk.LEFT, padx=5)
        self.zoom_scale = tk.Scale(zoom_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.zoom_timeline)
        self.zoom_scale.set(5)
        self.zoom_scale.pack(side=tk.LEFT, padx=5)

    def draw_timeline(self):
        self.timeline_canvas.delete("all")

        filtered_events = self.filter_events()
        self.event_ids = []
        for i, event in enumerate(filtered_events):
            color = "green" if event["type"] == "normal" else "red"
            y_position = (i + 1) * 30
            text_id = self.timeline_canvas.create_text(30, y_position, anchor='w', text=f"{event['time']} - {event['event']}", fill=color)
            oval_id = self.timeline_canvas.create_oval(10, y_position - 5, 20, y_position + 5, fill=color, outline="")
            self.event_ids.append((text_id, oval_id, event))

        self.timeline_canvas.config(scrollregion=self.timeline_canvas.bbox("all"))

    def filter_events(self):
        filter_type = self.filter_type.get()
        filter_date = self.filter_date.get()

        filtered_events = self.events

        if filter_type != "all":
            filtered_events = [e for e in filtered_events if e["type"] == filter_type]

        if filter_date:
            try:
                filter_date = datetime.strptime(filter_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                filtered_events = [e for e in filtered_events if e["time"].startswith(filter_date)]
            except ValueError:
                messagebox.showerror("Invalid Date", "Date format should be YYYY-MM-DD.")
        
        return filtered_events

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        for text_id, oval_id, event_data in self.event_ids:
            text_bbox = self.timeline_canvas.bbox(text_id)
            oval_bbox = self.timeline_canvas.bbox(oval_id)

            if (text_bbox[0] <= x <= text_bbox[2] and text_bbox[1] <= y <= text_bbox[3]) or \
               (oval_bbox[0] <= x <= oval_bbox[2] and oval_bbox[1] <= y <= oval_bbox[3]):
                self.show_event_details(event_data)
                break

    def show_event_details(self, event_details):
        messagebox.showinfo("Event Details", f"Time: {event_details['time']}\nEvent: {event_details['event']}\nType: {event_details['type']}")

    def zoom_timeline(self, zoom_value):
        scale = int(zoom_value)
        self.timeline_canvas.scale("all", 0, 0, scale / 5.0, 1)  
        self.timeline_canvas.config(scrollregion=self.timeline_canvas.bbox("all"))

    def update_timeline(self, event=None):
        self.draw_timeline()

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()  
    timeline = Timeline(root)
    timeline.show()
    root.mainloop()
