filename = input("Enter CSV file name: ")
dept_totals = {}
dept_counts = {}

with open(filename, 'r') as f:
    for line in f:
        name, dept, salary = line.strip().split(',')
        salary = int(salary)
        if dept in dept_totals:
            dept_totals[dept] += salary
            dept_counts[dept] += 1
        else:
            dept_totals[dept] = salary
            dept_counts[dept] = 1

print("Department\tAverage Salary")
for dept in dept_totals:
    avg = dept_totals[dept] / dept_counts[dept]
    print(f"{dept}\t\t{avg:.2f}")