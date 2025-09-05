#!/usr/bin/env python3
import sys
if sys.platform == "darwin":
    import os
    os.environ["TK_SILENCE_DEPRECATION"] = "1"
import os
from mutagen import File
import tkinter as tk
from tkinter import filedialog, font, messagebox
try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
    DND_AVAILABLE = True
except ImportError:
    DND_AVAILABLE = False

import re






# Allowed audio extensions
ALLOWED_EXT = {".wav", ".mp3"}

# --- Audio processing functions ---

def main():
    # Use TkinterDnD.Tk if available, else fallback to tk.Tk
    root = TkinterDnD.Tk() if DND_AVAILABLE else tk.Tk()
    root.title("Audio Length Calculator")
    root.geometry("600x400")  # Make window larger
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=14)
    root.option_add("*Font", default_font)

    def open_file_dialog():
        file_paths = filedialog.askopenfilenames(title="Select Audio Files")
        if file_paths:
            show_audio_lengths(file_paths)

    def show_audio_lengths(file_paths):
        # TkinterDnD passes a single string, not a list
        if isinstance(file_paths, (list, tuple)):
            file_paths = ' '.join(file_paths)
        # Use regex to extract all paths inside braces, or split by spaces if no braces
        import re
        paths = re.findall(r'\{([^}]+)\}', file_paths)
        if not paths:
            paths = file_paths.split()
        print("Received file paths:", paths)  # Debug print
        total_length = 0
        counted = 0
        ignored = 0
        for file_path in paths:
            file_path = file_path.strip()
            ext = os.path.splitext(file_path)[1].lower()
            if ext not in ALLOWED_EXT:
                ignored += 1
                continue
            try:
                audio = File(file_path)
                if audio is None or not hasattr(audio.info, 'length'):
                    ignored += 1
                    continue
                total_length += audio.info.length
                counted += 1
            except Exception as e:
                ignored += 1
                print(f"Error reading {file_path}: {e}")
        if counted == 0:
            result = "No valid audio files found."
        else:
            hours = int(total_length // 3600)
            minutes = int((total_length % 3600) // 60)
            seconds = int(total_length % 60)
            finished_hours = total_length / 3600
            result = (
                f"Total Length: {hours} Hours {minutes} Minutes {seconds} Seconds\n"
                f"Finished Hours: {finished_hours:.2f}\n"
                f"Files counted: {counted}\n"
                f"Files ignored: {ignored}"
            )
        result_label.config(text=result)

    open_button = tk.Button(root, text="Open Audio Files", command=open_file_dialog)
    open_button.pack(pady=20)

    result_label = tk.Label(root, text="Length: ", font=(None, 16))
    result_label.pack(pady=10)

    def reset_result():
        result_label.config(text="Length: ")

    reset_button = tk.Button(root, text="Reset", command=reset_result)
    reset_button.pack(pady=5)

    # Add drag-and-drop area if DND is available
    if DND_AVAILABLE:
        drop_label = tk.Label(root, text="Or drag and drop audio files here", relief="groove", width=45, height=6, bg="#2C3E50", fg="white", font=(None, 16))
        drop_label.pack(pady=15)
        def drop(event):
            files = event.data.strip().split()
            cleaned_files = []
            for f in files:
                if f.startswith('{') and f.endswith('}'):
                    f = f[1:-1]
                cleaned_files.append(f)
            show_audio_lengths(cleaned_files)
        drop_label.drop_target_register(DND_FILES)
        drop_label.dnd_bind('<<Drop>>', drop)

    root.mainloop()

# Launch the GUI when run as a script or command
if __name__ == "__main__":
    main()

