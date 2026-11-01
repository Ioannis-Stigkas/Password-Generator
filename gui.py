import random
import string
import tkinter as tk
from tkinter import messagebox


def generate():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Length must be a number.")
        return

    if length < 1:
        messagebox.showerror("Error", "Length must be at least 1.")
        return

    characters = string.ascii_letters

    if digits_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())


def paste_password():
    try:
        text = root.clipboard_get()
    except tk.TclError:
        return
    password_entry.delete(0, tk.END)
    password_entry.insert(0, text)


def check():
    password = password_entry.get()
    problems = []

    if len(password) < 8:
        problems.append("at least 8 characters")
    if not any(c in string.ascii_uppercase for c in password):
        problems.append("an uppercase letter")
    if not any(c in string.ascii_lowercase for c in password):
        problems.append("a lowercase letter")
    if not any(c in string.digits for c in password):
        problems.append("a digit")
    if not any(c in string.punctuation for c in password):
        problems.append("a symbol")

    if problems:
        result_label.config(text="Weak. Missing: " + ", ".join(problems), fg="red")
    else:
        result_label.config(text="Strong password!", fg="green")


root = tk.Tk()
root.title("Password Generator")
root.geometry("350x420")

BG = "#34BD5D"
FG = "#ecf404"
ENTRY_BG = "#7CCBCE"
BUTTON_BG = "#ca3bf6"

root.configure(bg=BG)

root.option_add("*Font", "verdana 10")
root.option_add("*Background", BG)
root.option_add("*Foreground", FG)
root.option_add("*Entry.Background", ENTRY_BG)
root.option_add("*Entry.insertBackground", FG)
root.option_add("*Button.Background", BUTTON_BG)
root.option_add("*Button.activeBackground", "#A00000")
root.option_add("*Button.activeForeground", FG)
root.option_add("*Checkbutton.selectColor", ENTRY_BG)
root.option_add("*Checkbutton.activeBackground", BG)
root.option_add("*Checkbutton.activeForeground", FG)

tk.Label(root, text="Password length:").pack(pady=(15, 0))
length_entry = tk.Entry(root, width=10)
length_entry.insert(0, "12")
length_entry.pack()

digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(root)
options_frame.pack(pady=(10, 0))

tk.Checkbutton(options_frame, text="Digits", variable=digits_var,
               font=("Segoe UI", 12), cursor="hand2").pack(side="left", padx=10)
tk.Checkbutton(options_frame, text="Symbols", variable=symbols_var,
               font=("Segoe UI", 12), cursor="hand2").pack(side="left", padx=10)
tk.Button(root, text="Generate", command=generate).pack(pady=10)

result_entry = tk.Entry(root, width=35, justify="center")
result_entry.pack()

tk.Button(root, text="Copy", command=copy_password).pack(pady=10)

tk.Label(root, text="Check a password:").pack(pady=(15, 0))
password_entry = tk.Entry(root, width=35)
password_entry.pack()
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="Paste", command=paste_password).pack(side="left", padx=5)
tk.Button(buttons_frame, text="Check", command=check).pack(side="left", padx=5)
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

root.mainloop()