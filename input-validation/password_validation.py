password = input("Enter your password: ")

if (
    len(password) >= 8
    and password.isalnum()
    and not password.isalpha()
    and not password.isdigit()
):
    print("Password format is valid.")
else:
    print("Password format is invalid.")
