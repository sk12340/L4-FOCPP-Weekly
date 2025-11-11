day_number = int(input("Enter a number (1-7): "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 1 <= day_number <= 7:
    print(f"Day {day_number} is {days[day_number-1]}")
else:
    print("Invalid input! Please enter number between 1-7")