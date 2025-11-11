number = int(input("Which times table do you require (0-12)? "))
if 0 <= number <= 12:
    for i in range(0, 13):
        print(i, "x", number, "=", i * number)
else:
    print("Invalid number. Please enter a number between 0 and 12.")