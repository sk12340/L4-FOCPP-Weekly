temperatures = []
while True:
    temp_input = input("Enter a temperature (e.g., 25C) or press Enter to finish: ")
    if temp_input == "":
        break
    # Extract the number part and convert to float
    temp_value = float(temp_input[:-1])
    temperatures.append(temp_value)

if temperatures:  # Check if the list is not empty
    print("Maximum:", max(temperatures))
    print("Minimum:", min(temperatures))
    print("Mean:", sum(temperatures) / len(temperatures))
else:
    print("No temperatures were entered.")