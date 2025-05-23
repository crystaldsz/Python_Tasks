# Password Strength Checker
# Check if a password is strong (has uppercase, lowercase, digits, and special characters).

# Determines and prints the strength of a given password.
def check_password_strength(password):
    pwd_length = len(password)
    has_lower = False
    has_upper = False
    has_digit = False
    has_special_char = False

    # Check each character in the password.
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        # If it's not a letter or a digit, it must be a special character.
        elif not char.isalnum(): 
            has_special_char = True

    print("Strength of password:- ", end = "")
    if (has_lower and has_upper and
        has_digit and has_special_char and pwd_length >= 8):
        print("Strong")
    elif ((has_lower or has_upper) and
          has_special_char and pwd_length >= 6):
        print("Moderate")
    else:
        print("Weak")

if __name__=="__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)