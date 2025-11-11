password1 = input("Enter a new password (8-12 chars): ")
if len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters long.")
else:
    password2 = input("Enter the password again: ")
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match.")