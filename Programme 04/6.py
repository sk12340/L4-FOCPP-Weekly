temp_input = input("Enter a temperature (e.g., 25C): ")
if temp_input[-1].upper() == 'C':
    celsius = float(temp_input[:-1])
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equivalent to {fahrenheit}F.")
else:
    print("Invalid format. Please use a number followed by 'C'.")