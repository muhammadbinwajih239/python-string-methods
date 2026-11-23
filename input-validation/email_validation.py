email = input("Enter your email address: ")

email = email.strip()

at_count = email.count("@")
at_position = email.find("@")
dot_position = email.find(".", at_position)

if (
    at_count == 1
    and at_position > 0
    and dot_position > at_position + 1
    and dot_position < len(email) - 1
    and " " not in email
):
    print(f"Valid email format: {email}")
else:
    print("Invalid email format.")
