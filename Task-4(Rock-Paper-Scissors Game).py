# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:55:55 2024

@author: bhask
"""

import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    print(result)

def play_game():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ('rock', 'paper', 'scissors'):
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
