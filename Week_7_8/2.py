def safe_int_input():
    while True:
        try:
            n = int(input("Enter an integer: "))
            return n
        except ValueError:
            print("Invalid! Enter an integer.")

num = safe_int_input()
print(f"You entered: {num}")