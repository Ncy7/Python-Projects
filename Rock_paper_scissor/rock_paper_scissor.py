# Rock paper scissor
# Project 2
import random

choices = ["rock","paper","scissors"]
print("Welcome to Rock Paper Scissors!")
user_choice = input("Enter your choice: ")
computer_choice = random.choices(choices)
print(f"Computer choice is {computer_choice}")
print(f"User choice is {user_choice}")