import tkinter as tk
import random

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n"

    if user_choice == computer_choice:
        result_text += "🤝 It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_text += "🎉 You Win!"
        user_score += 1
    else:
        result_text += "💻 Computer Wins!"
        computer_score += 1

    result_label.config(text=result_text)
    score_label.config(text=f"🏆 Your Score: {user_score}   💻 Computer Score: {computer_score}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.config(bg="#f4f4f4")

title = tk.Label(root, text="✊ Rock ✋ Paper ✌ Scissors", font=("Arial", 16, "bold"), bg="#f4f4f4")
title.pack(pady=15)

instruction = tk.Label(root, text="Choose your move:", font=("Arial", 12), bg="#f4f4f4")
instruction.pack(pady=5)

btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack()

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock"), bg="#E57373", fg="white")
paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper"), bg="#64B5F6", fg="white")
scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors"), bg="#81C784", fg="white")

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f4", wraplength=300, justify="center")
result_label.pack(pady=20)

score_label = tk.Label(root, text="🏆 Your Score: 0   💻 Computer Score: 0", font=("Arial", 12, "bold"), bg="#f4f4f4")
score_label.pack(pady=10)

root.mainloop()
