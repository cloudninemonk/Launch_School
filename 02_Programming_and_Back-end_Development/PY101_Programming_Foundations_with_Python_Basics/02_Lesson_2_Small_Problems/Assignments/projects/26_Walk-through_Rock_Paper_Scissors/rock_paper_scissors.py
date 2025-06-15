"""Allows for the implementation of random choice by the computer."""
import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

# def prompt(message):
#     """Standardises outputs from the program."""
#     print(f'==> {message}')

def display_winner(player, computer):
    """Displays the winner based on the player and computer choices."""
    prompt(f"You chose {user_choice}, the computer chose {computer_choice}.")
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        # prompt("You win!")
        return "You win"
    elif ((player == 'rock' and computer == 'paper') or
          (player == 'paper' and computer == 'scissors') or
          (player == 'scissors' and computer == 'rock')):
        # prompt("Computer wins!")
        return "You win"
    else:
        # prompt("It's a tie!")
        return "It's a tie"

def prompt(message):
    """Standardises outputs from the program."""
    print(f'==> {message}')

prompt("Welcome to rock, paper, scissors.")
while True:

    prompt(f"Choose one of the following moves: {' ,'.join(VALID_CHOICES)}")
    user_choice = input()

    while user_choice not in VALID_CHOICES:
        prompt("You entered an invalid move. Try again.")
        user_choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    print(display_winner(user_choice, computer_choice))

    answer = ''
    while not (answer.startswith('y') or answer.startswith('n')):
        prompt("Would you like to play again? (y/n)")
        answer = input().lower()
        if not (answer.startswith('y') or answer.startswith('n')):
            prompt("Provide a valid response.")

    if answer[0] == 'n':
        break
