try:
    nums = input("Enter numbers separated by space: ").split()
    if len(nums) < 2:
        raise ValueError("At least two numbers required.")
    
    numbers = []
    for n in nums:
        numbers.append(float(n))
    
    numbers = list(set(numbers))  # remove duplicates
    numbers.sort(reverse=True)
    
    if len(numbers) >= 2:
        print("Second largest:", numbers[1])
    else:
        print("No second largest.")
        
except ValueError as e:
    print("Error:", e)