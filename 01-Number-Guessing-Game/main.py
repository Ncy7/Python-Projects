# 01-Number Guessing Game
# main.py

import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Generate a random secret number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        guess_input = input("\nEnter your guess: ")
        guess = int(guess_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f" Correct! you got it in {attempts} attempts!") # f inside the bracket denotes the formatted string
            break #Exit loop - player won!

if __name__ == "__main__":
    main()