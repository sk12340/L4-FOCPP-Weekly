import math

print("Choose operation:")
print("1. Square root")
print("2. Absolute value")
print("3. Floor division")
print("4. Percentage")
print("5. Average")

choice = input("Enter choice (1-5): ")

if choice == '1':
    n = float(input("Enter number: "))
    print("Square root:", math.sqrt(n))
elif choice == '2':
    n = float(input("Enter number: "))
    print("Absolute value:", abs(n))
elif choice == '3':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Floor division:", a // b)
elif choice == '4':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Percentage:", (a / b) * 100)
elif choice == '5':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Average:", (a + b) / 2)
else:
    print("Invalid choice.")