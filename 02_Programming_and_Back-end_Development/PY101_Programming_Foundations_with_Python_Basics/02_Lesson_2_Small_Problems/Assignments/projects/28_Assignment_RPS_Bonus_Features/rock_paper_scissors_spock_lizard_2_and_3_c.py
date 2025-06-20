"""Allows for the implementation of random choice by the computer."""

import random

# VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'sp': 'spock',
    'l': 'lizard'
}

WINNING_COMBOS = {
    'r': ['s', 'l'],      # rock beats scissors and lizard
    'p': ['r', 'sp'],     # paper beats rock and spock
    's': ['p', 'l'],      # scissors beats paper and lizard
    'sp': ['s', 'r'],     # spock beats scissors and rock
    'l': ['sp', 'p']      # lizard beats spock and paper
}

def display_winner(player, computer):
    """Displays the winner based on the player and computer choices."""
    if computer in WINNING_COMBOS[player]:
        return "You win"
    elif player in WINNING_COMBOS[computer]:
        return "Computer wins"
    else:
        return "It's a tie"

def match_points(winner, score):
    """Calculates each players score."""
    if winner == "You win":
        score['player'] += 1
    elif winner == "Computer wins":
        score['computer'] += 1

def match_winner(score):
    """Determines if there is a match winner after each game."""
    if score['player'] == 3:
        prompt("YOU WON THE MATCH. WOOOOOO!")
    elif score['computer'] == 3:
        prompt("Computer won the match!")

def end_match(score):
    """Prompt to end the game if there is a winner."""
    return score['player'] == 3 or score['computer'] == 3

def prompt(message):
    """Standardises outputs from the program."""
    print(f'==> {message}')

prompt("Welcome to Rock, Paper, Scissors, Spock, Lizard!" \
"The first to 3 is the winner.")

while True:
    match_score = {'player': 0, 'computer': 0}

    while True:
        user_choice = ''
        while not user_choice.startswith(tuple(VALID_CHOICES)):
            prompt("Choose one of the following moves:")
            for (key, value) in VALID_CHOICES.items():
                prompt(f"'{key}' for '{value}'")
            user_choice = input().lower()[0]
            if user_choice not in list(VALID_CHOICES):
                prompt("Provide a valid response.")

        computer_choice = random.choice(list(VALID_CHOICES))

        prompt(f"You chose '{user_choice}', the computer chose '{computer_choice}'.")

        result = display_winner(user_choice, computer_choice)
        prompt(result)

        match_points(result, match_score)

        prompt(f"The score is {match_score}")

        match_winner(match_score)
        if end_match(match_score):
            break

    answer = ''
    while not (answer.startswith('y') or answer.startswith('n')):
        prompt("Would you like to play another match? (y/n)")
        answer = input().lower()
        if not (answer.startswith('y') or answer.startswith('n')):
            prompt("Provide a valid response.")

    if answer[0] == 'n':
        break
