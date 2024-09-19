import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog
import os
import hashlib

class EvidenceImport:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.frame, text="Evidence Import", font=("Arial", 18, "bold"), bg="#f0f0f0")
        label.pack(pady=10, fill=tk.X)

        self.upload_area = ttk.Frame(self.frame, relief="sunken", width=400, height=200)
        self.upload_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.upload_area.bind("<Button-1>", self.select_files)  

        self.upload_area_label = tk.Label(
            self.upload_area, 
            text="Drag and Drop Files Here\nor Click to Select Files", 
            font=("Arial", 12), 
            padx=20, pady=20,
            bg="#e0e0e0",  
            relief="flat"
        )
        self.upload_area_label.pack(expand=True, fill=tk.BOTH)

        self.supported_formats_label = tk.Label(self.frame, text="Supported Formats: RAW, E01, AFF, etc.", font=("Arial", 10), bg="#f0f0f0")
        self.supported_formats_label.pack(pady=5)

        self.progress_frame = ttk.Frame(self.frame)
        self.progress_frame.pack(pady=10, fill=tk.X)

        self.progress_label = tk.Label(self.progress_frame, text="Upload Progress:", font=("Arial", 10))
        self.progress_label.pack(side=tk.LEFT)

        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(side=tk.LEFT, padx=10)

        self.metadata_frame = ttk.Frame(self.frame)
        self.metadata_frame.pack(pady=10, fill=tk.X)

        self.metadata_label = tk.Label(self.metadata_frame, text="Metadata will appear here.", font=("Arial", 10), bg="#f9f9f9", relief="sunken", padx=10, pady=10)
        self.metadata_label.pack(fill=tk.BOTH)

        self.frame.drop_target_register(DND_FILES)
        self.frame.dnd_bind('<<Drop>>', self.on_drop)

    def select_files(self, event=None):
        file_paths = filedialog.askopenfilenames(
            title="Select Evidence Files",
            filetypes=[("All Files", "*.*")]
        )
        if file_paths:
            self.handle_files(file_paths)

    def on_drop(self, event):
        files = self.frame.tk.splitlist(event.data)
        if files:
            self.handle_files(files)

    def handle_files(self, files):
        for file_path in files:
            if os.path.isfile(file_path):
                self.show_metadata(file_path)
                self.process_file(file_path)

    def process_file(self, file_path):
        file_size = os.path.getsize(file_path)
        self.progress_bar["maximum"] = file_size
        self.progress_bar["value"] = 0

        chunk_size = 1024 
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                self.progress_bar["value"] += chunk_size
                self.frame.update_idletasks() 

    def show_metadata(self, file_path):
        file_size = os.path.getsize(file_path)
        file_hash = self.get_file_hash(file_path)
        metadata_text = (
            f"File Name: {os.path.basename(file_path)}\n"
            f"Size: {file_size} bytes\n"
            f"Hash: {file_hash}\n"
            f"Date: {os.path.getmtime(file_path)}"
        )
        self.metadata_label.config(text=metadata_text)

    def get_file_hash(self, file_path, algorithm="sha256"):
        hash_algo = hashlib.new(algorithm)
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    evidence_import = EvidenceImport(root)
    evidence_import.show()
    root.mainloop()
