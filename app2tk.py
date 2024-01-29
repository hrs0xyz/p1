import os
import pandas as pd
from tkinter import Tk, Label, Button, OptionMenu, StringVar, filedialog, Frame, ttk

class FileUploadApp:
    def __init__(self, master):
        self.master = master
        master.title("File Upload and Processing")

        self.selected_type = StringVar(master)
        self.selected_type.set("type1")  # Default type

        self.frame = Frame(master)
        self.frame.pack()

        self.create_navbar()
        self.create_type_selection()
        self.create_upload_section()
        self.create_processing_bar()
        self.create_download_button()

    def create_navbar(self):
        Label(self.frame, text="HOME", bg="#333", fg="white", width=50).grid(row=0, column=0, columnspan=5, sticky="ew")

    def create_type_selection(self):
        Label(self.frame, text="Select type:", pady=5).grid(row=1, column=0, padx=10, pady=5)
        OptionMenu(self.frame, self.selected_type, "type1", "type2").grid(row=1, column=1, padx=10, pady=5)

    def create_upload_section(self):
        self.file_paths = []
        self.upload_frame = Frame(self.frame)
        self.upload_frame.grid(row=2, column=0, columnspan=2, pady=10)

        Button(self.upload_frame, text="Choose Excel Files", command=self.choose_files).pack(pady=5)
        Label(self.upload_frame, text="Selected Files:").pack()

    def choose_files(self):
        file_count = 3 if self.selected_type.get() == "type1" else 4
        file_paths = filedialog.askopenfilenames(title="Select Excel Files", filetypes=[("Excel files", "*.xlsx")])

        if len(file_paths) == file_count:
            self.file_paths = file_paths
            self.update_file_list()
        else:
            print(f"Please select {file_count} Excel files.")

    def update_file_list(self):
        for widget in self.upload_frame.winfo_children():
            widget.destroy()

        Button(self.upload_frame, text="Choose Excel Files", command=self.choose_files).pack(pady=5)
        Label(self.upload_frame, text="Selected Files:").pack()

        for file_path in self.file_paths:
            Label(self.upload_frame, text=os.path.basename(file_path)).pack()

        Button(self.upload_frame, text="Submit", command=self.process_files).pack(pady=5)

    def create_processing_bar(self):
        self.progress_var = StringVar()
        self.progress_var.set("")

        self.processing_frame = Frame(self.frame)
        self.processing_frame.grid(row=3, column=0, columnspan=2, pady=10)

        Label(self.processing_frame, text="Processing Status:").pack()
        ttk.Progressbar(self.processing_frame, mode="indeterminate", variable=self.progress_var).pack(pady=5)

    def process_files(self):
        # Add your processing logic here
        # For demonstration, just updating the processing bar
        self.progress_var.set("Processing...")

        # Simulate processing delay
        self.master.after(3000, self.processing_complete)

    def processing_complete(self):
        self.progress_var.set("Processing Complete!")

    def create_download_button(self):
        Button(self.frame, text="Download Result", command=self.download_result).grid(row=4, column=0, columnspan=2, pady=10)

    def download_result(self):
        # Add your logic to download the processed result
        # For demonstration, just updating the download button text
        Button(self.frame, text="Download Result (Completed)", state="disabled").grid(row=4, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = FileUploadApp(root)
    root.mainloop()
