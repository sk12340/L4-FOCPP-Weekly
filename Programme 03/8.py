number = int(input("Which times table do you require (e.g., 7 or -7)? "))
if number >= 0:
    for i in range(0, 13):
        print(i, "x", number, "=", i * number)
else:
    # If number is negative, print from 12 down to 0
    for i in range(12, -1, -1):
        print(i, "x", abs(number), "=", i * abs(number))