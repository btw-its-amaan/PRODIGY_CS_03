import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    error_messages = [
        "Password should be at least 8 characters long.",
        "Password should contain at least one digit.",
        "Password should contain at least one uppercase letter.",
        "Password should contain at least one lowercase letter.",
        "Password should contain at least one special character."
    ]

    strength = sum(1 for error in errors if not error)

    if strength == 5:
        return "Strong password"
    else:
        return "Weak password. " + ", ".join([error_messages[i] for i in range(5) if errors[i]])

def main():
    password = input("Enter your password: ")
    print(check_password_strength(password))

if __name__ == "__main__":
    main()
