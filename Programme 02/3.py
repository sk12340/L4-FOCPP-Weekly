students = int(input("How many students? "))
group_size = int(input("Required group size? "))

num_groups = students // group_size
left_over = students % group_size

# Grammar fix
group_word = "groups" if num_groups != 1 else "group"
student_word = "students" if left_over != 1 else "student"

print("There will be", num_groups, group_word, "with", left_over, student_word, "left over.")