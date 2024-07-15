import re


def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1

    # Check for uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check for lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Determine strength based on score
    if score < 2:
        strength = "Very Weak"
    elif score < 3:
        strength = "Weak"
    elif score < 4:
        strength = "Moderate"
    elif score < 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback


def main():
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break

        strength, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {strength}")

        if feedback:
            print("Suggestions to improve:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("Excellent password!")

        print()  # Add a blank line for readability


if __name__ == "__main__":
    main()