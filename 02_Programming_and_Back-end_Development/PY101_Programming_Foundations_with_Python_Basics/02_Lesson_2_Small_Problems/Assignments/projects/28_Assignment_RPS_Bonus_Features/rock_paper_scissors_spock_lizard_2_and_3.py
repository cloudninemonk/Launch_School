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

def display_winner(player, computer):
    """Displays the winner based on the player and computer choices."""
    if ((player == 'r' and computer == 's') or
        (player == 'r' and computer == 'l') or
        (player == 'p' and computer == 'r') or
        (player == 'p' and computer == 'sp') or
        (player == 's' and computer == 'p') or
        (player == 's' and computer == 'l') or
        (player == 'sp' and computer == 's') or
        (player == 'sp' and computer == 'r') or
        (player == 'l' and computer == 'sp') or
        (player == 'l' and computer == 'p')):

        return "You win"
    elif ((player == 'r' and computer == 'p') or
        (player == 'r' and computer == 'sp') or
        (player == 'p' and computer == 's') or
        (player == 'p' and computer == 'l') or
        (player == 's' and computer == 'r') or
        (player == 's' and computer == 'sp') or
        (player == 'sp' and computer == 'p') or
        (player == 'sp' and computer == 'l') or
        (player == 'l' and computer == 'r') or
        (player == 'l' and computer == 's')):

        return "Computer wins"

def match_points(winner):
    """Updates the score at the end of each game."""
    global player_score
    global computer_score

    if winner == "You win":
        player_score += 1
    elif winner == "Computer wins":
        computer_score += 1

def match_winner(player_score, computer_score):
    """Determines if there is a match winner after each game."""
    if player_score == 3:
        prompt("YOU WON THE MATCH. WOOOOOO!")
    elif computer_score == 3:
        prompt("Computer won the match!")

def end_match(player_score, computer_score):
    """Prompt to end the game if there is a winner."""
    if player_score == 3 or computer_score == 3:
        return True

def prompt(message):
    """Standardises outputs from the program."""
    print(f'==> {message}')

prompt("Welcome to Rock, Paper, Scissors, Spock, Lizard!" \
"The first to 3 is the winner.")

while True:
    player_score = 0
    computer_score = 0

    while True:
        prompt("Choose one of the following moves:")
        for (key, value) in VALID_CHOICES.items():
            prompt(f"'{key}' for '{value}'")
        user_choice = input()

        while user_choice not in VALID_CHOICES.keys():
            prompt("You entered an invalid move. Try again.")
            user_choice = input()

        computer_choice = random.choice(list(VALID_CHOICES.keys()))
        prompt(f"You chose {user_choice}, the computer chose {computer_choice}.")
        prompt(display_winner(user_choice, computer_choice))
        match_points(display_winner(user_choice, computer_choice))
        prompt(f"The score is player {player_score} : {computer_score} computer")

        match_winner(player_score, computer_score)
        if end_match(player_score, computer_score):
            break

    answer = ''
    while not (answer.startswith('y') or answer.startswith('n')):
        prompt("Would you like to play another match? (y/n)")
        answer = input().lower()
        if not (answer.startswith('y') or answer.startswith('n')):
            prompt("Provide a valid response.")

    if answer[0] == 'n':
        break


