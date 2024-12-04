import re

def analyze_password(password):
    # Define password strength criteria
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }

    # Calculate the password strength score
    score = sum(criteria.values())
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Generate recommendations
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

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    strength, feedback = analyze_password(password)
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for tip in feedback:
            print(f"- {tip}")

def check_common_passwords(password):
    # Create a sample list of common passwords (or use a real dataset)
    common_passwords = [
        "123456", "password", "123456789", "qwerty", "12345678", 
        "12345", "1234567", "1234567890", "admin", "letmein"
    ]
    if password in common_passwords:
        return True
    return False

# Example usage
if check_common_passwords(password):
    print("Warning: This password is too common and unsafe to use.")

import math

def calculate_entropy(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
        charset_size += len("!@#$%^&*(),.?\":{}|<>")
    
    entropy = len(password) * math.log2(charset_size)
    return entropy

# Example usage
entropy = calculate_entropy(password)
print(f"Password Entropy: {entropy:.2f} bits")
