import tkinter as tk
from tkinter import messagebox
import re

# Password analysis function
def analyze_password(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }

    # Strength score
    score = sum(criteria.values())
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Feedback
    feedback = []
    if not criteria["length"]:
        feedback.append("Increase password length to at least 8 characters.")
    if not criteria["uppercase"]:
        feedback.append("Add at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Add at least one lowercase letter.")
    if not criteria["digit"]:
        feedback.append("Add at least one numeric digit.")
    if not criteria["special_char"]:
        feedback.append("Add at least one special character (e.g., !, @, #).")

    return strength, feedback

# GUI logic
def analyze_password_gui():
    password = entry.get()
    if not password.strip():
        messagebox.showwarning("Error", "Password cannot be empty!")
        return

    strength, feedback = analyze_password(password)
    result = f"Password Strength: {strength}\n"
    if feedback:
        result += "Suggestions:\n" + "\n".join(f"- {tip}" for tip in feedback)
    messagebox.showinfo("Password Analysis", result)

# Tkinter GUI setup
root = tk.Tk()
root.title("Password Analyzer")

# GUI components
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Analyze Password", command=analyze_password_gui)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
