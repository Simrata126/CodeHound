# ui.py (Tkinter Desktop UI)
import tkinter as tk
from tkinter import messagebox

def run_scan():
    target = entry.get()
    if target:
        messagebox.showinfo("Scan", f"Running vulnerability scan on {target}...")
        # Calling the scan function from scanner.py
    else:
        messagebox.showwarning("Input Error", "Please enter a valid target.")

app = tk.Tk()
app.title("Vulnerability Scanner Tool")

label = tk.Label(app, text="Enter Target URL or IP:")
label.pack(pady=10)
entry = tk.Entry(app, width=50)
entry.pack(pady=5)

button = tk.Button(app, text="Run Scan", command=run_scan)
button.pack(pady=20)

app.mainloop()
