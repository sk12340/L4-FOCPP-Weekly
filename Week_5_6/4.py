# csv_grades.py
filename = input("Enter CSV file name: ")

print("Name\tMark\tGrade")
print("-" * 30)
with open(filename, 'r') as f:
    for line in f:
        name, mark = line.strip().split(',')
        mark = int(mark)
        if mark >= 80:
            grade = 'A'
        elif mark >= 60:
            grade = 'B'
        else:
            grade = 'C'
        print(f"{name}\t{mark}\t{grade}")