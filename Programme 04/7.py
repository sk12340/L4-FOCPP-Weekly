temperatures = []
for i in range(6):
    temp_input = input(f"Enter temperature {i+1} (e.g., 25C): ")
    # Extract the number part and convert to float
    temp_value = float(temp_input[:-1])
    temperatures.append(temp_value)

print("Maximum:", max(temperatures))
print("Minimum:", min(temperatures))
print("Mean:", sum(temperatures) / len(temperatures))