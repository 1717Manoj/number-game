import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < number:
            result_label.config(text="📉 Too Low! Try again", fg="orange")
        elif guess > number:
            result_label.config(text="📈 Too High! Try again", fg="orange")
        else:
            result_label.config(text=f"🎉 Correct! Attempts: {attempts}", fg="green")
            messagebox.showinfo("Success", f"You guessed it in {attempts} attempts!")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


def reset_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Game Reset! Start guessing...", fg="blue")


# GUI Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x350")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(root, text="🎯 Guess the Number (1-100)",
                 font=("Arial", 16, "bold"),
                 fg="white", bg="#1e1e2f")
title.pack(pady=15)

# Entry
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Guess Button
guess_btn = tk.Button(root, text="Check Guess",
                      font=("Arial", 12, "bold"),
                      bg="#2563eb", fg="white",
                      command=check_guess)
guess_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Start guessing...",
                        font=("Arial", 12),
                        fg="white", bg="#1e1e2f")
result_label.pack(pady=20)

# Reset Button
reset_btn = tk.Button(root, text="🔄 Restart Game",
                      font=("Arial", 11),
                      bg="#f59e0b", fg="black",
                      command=reset_game)
reset_btn.pack(pady=10)

# Run
root.mainloop()