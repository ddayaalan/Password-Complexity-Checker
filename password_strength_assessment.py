
import re

def assess_password_strength(password):
    # Initialize strength score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short; it should be at least 8 characters.")
    elif 8 <= len(password) < 12:
        score += 1
        feedback.append("Password length is acceptable, but a longer password is stronger.")
    else:
        score += 2
        feedback.append("Good length for a strong password.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Consider adding uppercase letters for a stronger password.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Consider adding lowercase letters for a stronger password.")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Consider adding numbers for a stronger password.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Consider adding special characters for a stronger password.")

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Output results
    return {
        "strength": strength,
        "feedback": feedback
    }

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to test its strength: ")
    result = assess_password_strength(password)
    print(f"Password strength: {result['strength']}")
    for comment in result['feedback']:
        print(comment)
