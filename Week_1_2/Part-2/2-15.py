import random

answer = random.randint(1, 100)
attempts = 5

print("Welcome to the Number Guessing Game!")
print("Please guess a number between 1 and 100")
print(f"You have {attempts} attempts to guess it!")

for attempt in range(1, attempts + 1):
    guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
    
    if guess == answer:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")
        
    if attempt == attempts:
        print(f"\nGame Over! The correct number was {answer}")