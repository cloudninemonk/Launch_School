"""Allows for the implementation of random choice by the computer."""
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

# def prompt(message):
#     """Standardises outputs from the program."""
#     print(f'==> {message}')

def display_winner(player, computer):
    """Displays the winner based on the player and computer choices."""
    prompt(f"You chose {user_choice}, the computer chose {computer_choice}.")
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'rock' and computer == 'lizard') or
        (player == 'paper' and computer == 'rock') or
        (player == 'paper' and computer == 'lizard') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'scissors' and computer == 'lizard') or
        (player == 'spock' and computer == 'scissors') or
        (player == 'spock' and computer == 'rock') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'lizard' and computer == 'paper')):
        # prompt("You win!")
        return "You win"
    if ((player == 'rock' and computer == 'paper') or
        (player == 'rock' and computer == 'spock') or
        (player == 'paper' and computer == 'rock') or
        (player == 'paper' and computer == 'lizard') or
        (player == 'scissors' and computer == 'rock') or
        (player == 'scissors' and computer == 'spock') or
        (player == 'spock' and computer == 'paper') or
        (player == 'spock' and computer == 'lizard') or
        (player == 'lizard' and computer == 'rock') or
        (player == 'lizard' and computer == 'scissors')):
        # prompt("Computer wins!")
        return "You win"

    # prompt("It's a tie!")
    return "It's a tie"

def prompt(message):
    """Standardises outputs from the program."""
    print(f'==> {message}')

prompt("Welcome to Rock Paper Scissor Spock Lizard.")

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
