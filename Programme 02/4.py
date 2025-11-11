total_sweets = int(input("How many sweets are in the tub? "))
num_pupils = int(input("How many pupils are present today? "))

sweets_per_pupil = total_sweets // num_pupils
left_over_sweets = total_sweets % num_pupils

print("Give each pupil", sweets_per_pupil, "sweets.")
print("You will have", left_over_sweets, "sweets left over.")