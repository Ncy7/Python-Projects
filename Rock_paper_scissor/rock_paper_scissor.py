# Rock paper scissor
# Project 2
import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors!")
user_choice = input("Enter your choice: ").lower().strip()  #.lower() so ROCK or Rock still works  &  .strip() removes accidental spaces
# computer_choice = random.choices(choices) # It return a list with one or more items (with replacement). So I get ['rock']
computer_choice = random.choice(choices)  # (singular) -> returns just the string

print(f"Computer choice: {computer_choice}")
print(f"User choice: {user_choice}")