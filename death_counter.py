import tkinter as tk
from tkinter import filedialog
import keyboard
import os

class DeathCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Death Counter")

        self.count = 0
        self.file_path = None  # เก็บ path ของไฟล์ txt

        # Label
        self.label = tk.Label(root, text=f"Deaths: {self.count}", font=("Arial", 24))
        self.label.pack(pady=20)


        # Input
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10,padx=20)

        self.set_btn = tk.Button(root, text="Set Count", command=self.set_count)
        self.set_btn.pack(pady=5)


        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)


        self.set_btnplus = tk.Button(btn_frame, text="+", command=self.increment)
        self.set_btnplus.grid(row=0, column=0, padx=5, pady=5)

        self.set_btndown = tk.Button(btn_frame, text="-", command=self.decrement)
        self.set_btndown.grid(row=0, column=1, padx=5, pady=5)

        
        other_frame = tk.Frame(root)
        other_frame.pack(pady=10)

        self.reset_btn = tk.Button(other_frame, text="Reset", command=self.reset)
        self.reset_btn.pack(pady=5)


        self.file_btn = tk.Button(other_frame, text=".txt Output", command=self.choose_file)
        self.file_btn.pack(pady=5)

        # Hotkeys
        keyboard.add_hotkey("ctrl+shift+page up", self.increment)
        keyboard.add_hotkey("ctrl+shift+page down", self.decrement)

    def choose_file(self):
        """เลือกไฟล์ .txt เพื่อใช้เก็บค่า"""
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if file:
            self.file_path = file
            if os.path.exists(file):
                with open(file, "r") as f:
                    try:
                        self.count = int(f.read().strip())
                    except ValueError:
                        self.count = 0
            self.update_label()
            self.save_to_file()

    def increment(self):
        self.count += 1
        self.update_label()
        self.save_to_file()

    def reset(self):
        self.count = 0
        self.update_label()
        self.save_to_file()

    def decrement(self):
        if self.count > 0:
            self.count -= 1
        self.update_label()
        self.save_to_file()

    def set_count(self):
        try:
            value = int(self.entry.get())
            if value >= 0:
                self.count = value
                self.update_label()
                self.save_to_file()
        except ValueError:
            pass

    def update_label(self):
        self.label.config(text=f"Deaths: {self.count}")

    def save_to_file(self):
        if self.file_path:
            with open(self.file_path, "w") as f:
                f.write(str(self.count))

if __name__ == "__main__":
    root = tk.Tk()
    app = DeathCounter(root)
    root.mainloop()
