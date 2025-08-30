import re

def check_password(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()_+]", password) is None

    if length_error or digit_error or uppercase_error or lowercase_error or symbol_error:
        print("Weak password")
        if length_error:
            print("- Too short (min 8 chars)")
        if digit_error:
            print("- Missing a number")
        if uppercase_error:
            print("- Missing an uppercase letter")
        if lowercase_error:
            print("- Missing a lowercase letter")
        if symbol_error:
            print("- Missing a special symbol (!@#$%^&*()_+)")
    else:
        print("Strong password!")

pw = input("Enter password to check: ")
check_password(pw)
