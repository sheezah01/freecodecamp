import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry! Too low.")
        elif guess > random_number:
            print("Sorry! Too high.")
    print(f"You guessed it right! The number was {random_number}.")

guess(10)
