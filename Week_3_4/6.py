unique = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num not in unique:
        unique.append(num)

unique.sort()
print("Unique numbers:", unique)