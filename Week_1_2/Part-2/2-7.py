celsius = float(input("Enter temperature in Celsius: "))

if celsius < 10:
    print("Cold")
elif 10 <= celsius <= 25:
    print("Warm")
else:
    print("Hot")