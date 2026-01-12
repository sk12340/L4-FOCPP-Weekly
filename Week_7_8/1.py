try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter numbers only.")