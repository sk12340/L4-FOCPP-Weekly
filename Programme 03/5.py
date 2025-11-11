BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password1 = input("Enter a new password (8-12 chars): ")
    if len(password1) < 8 or len(password1) > 12:
        print("Error: Password must be between 8 and 12 characters long.")
        continue
    if password1 in BAD_PASSWORDS:
        print("Error: That password is too common.")
        continue
    password2 = input("Enter the password again: ")
    if password1 == password2:
        print("Password Set")
        break
    else:
        print("Error: Passwords do not match.")