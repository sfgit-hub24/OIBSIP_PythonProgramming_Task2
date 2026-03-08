#-----------------------------------------------------------------------------------
# Random Password Generator with Strength Analysis + Clipboard (GUI Version)
#-----------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import random
import string

#-----------------------------------------------------------------------------------
# Generate Password Function
# ----------------------------------------------------------------------------------
def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")
        return

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return

    pool = ""

    if lower_var.get():
        pool += string.ascii_lowercase
    if upper_var.get():
        pool += string.ascii_uppercase
    if digit_var.get():
        pool += string.digits
    if symbol_var.get():
        pool += string.punctuation

    if pool == "":
        messagebox.showwarning("Error", "Select at least one character type")
        return

    password = ''.join(random.choice(pool) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)

# ----------------------------------------------------------------------------------
# Password Strength Checker
# ----------------------------------------------------------------------------------
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak")
    elif score <= 4:
        strength_label.config(text="Strength: Medium")
    else:
        strength_label.config(text="Strength: Strong")

# ----------------------------------------------------------------------------------
# Copy Password to Clipboard
# ----------------------------------------------------------------------------------
def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "No password to copy")
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------------------------------------------------------------------------
# GUI Window Setup
# ---------------------------------------------------------------------------------
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="lavender")

# ---------------------------------------------------------------------------------
# Password Length Input
# ---------------------------------------------------------------------------------
tk.Label(root, text="Password Length", font=("Arial", 10)).pack(pady=5)

length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, width=10).pack()

# ---------------------------------------------------------------------------------
# Character Options
# ---------------------------------------------------------------------------------
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var).pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var).pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=digit_var).pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Include Symbols (!@#)", variable=symbol_var).pack(anchor="w", padx=100)

# ---------------------------------------------------------------------------------
# Generate Button
# ---------------------------------------------------------------------------------
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# ---------------------------------------------------------------------------------
# Password Display
# ---------------------------------------------------------------------------------
password_entry = tk.Entry(root, width=30, justify="center", font=("Arial", 12))
password_entry.pack(pady=5)

# ---------------------------------------------------------------------------------
# Strength Indicator
# ---------------------------------------------------------------------------------
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 10))
strength_label.pack(pady=5)

# ---------------------------------------------------------------------------------
# Copy Button
# ---------------------------------------------------------------------------------
tk.Button(root, text="Copy Password", command=copy_password).pack(pady=10)

# ---------------------------------------------------------------------------------
# Run Application
# ---------------------------------------------------------------------------------
root.mainloop()
