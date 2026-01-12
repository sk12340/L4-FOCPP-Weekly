student_names = {1: 'Anish', 2: 'Priya', 3: 'Sujan'}
student_scores = {1: 88, 2: 92, 3: 79}

merged = {}
for key in student_names:
    name = student_names[key]
    score = student_scores[key]
    merged[name] = score

print("Merged dictionary:", merged)