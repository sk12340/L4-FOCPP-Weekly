import random

print("Password Checker")
print("=================\n")

pwd = input("Hey user enter a password: ")

if len(pwd) < 9:
    print("Password too short")
    exit()

for i in range(3):
    position = random.randint(1, len(pwd))
    guess = input(f"\nEnter letter at position {position}: ")

    if guess == pwd[position-1]:
        print("\nCorrect")

    else:
        print("\nSecurity Check Failed")
        exit()

print("\nSecurity check passed")            