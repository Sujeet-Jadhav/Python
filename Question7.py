import re
def is_valid_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    if re.match(pattern, password):
        return True
    else:
        return False
password_input = input("Enter your password: ")
if(is_valid_password(password_input)):
    print("Valid password!")
else:
    print("Invalid password. Make sure it has at least 8 characters, one uppercase letter, one lowercase letter, and one digit.");