numbers = input("Enter numbers separated by space: ").split()
num_list = []
for n in numbers:
    num_list.append(int(n))

evens = []
for n in num_list:
    if n % 2 == 0:
        evens.append(n)

evens.sort()
print("Even numbers sorted:", evens)