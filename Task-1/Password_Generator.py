import tkinter as tk
from tkinter import messagebox
import string
import secrets

def password_strength(length):
    if length < 6:
        return "Weak"
    elif 6 <= length < 10:
        return "Moderate"
    else:
        return "Strong"

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password:\n{password}")
        strength = password_strength(length)
        strength_label.config(text=f"Password Strength: {strength}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry_label = tk.Label(root, text="Enter password length:", bg="#f0f0f0")
entry_label.pack()
entry = tk.Entry(root, width=10, justify='center')
entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 10), wraplength=350, bg="#f0f0f0")
result_label.pack(pady=5)

strength_label = tk.Label(root, text="", font=("Arial", 10, "italic"), bg="#f0f0f0")
strength_label.pack()

root.mainloop()
