'''
High level breakdown:

1. Display the initial empty 3x3 board.
2. Ask the user to mark a square.
3. Computer marks a square.
4. Display the updated board state.
5. If it's a winning board, display the winner.
6. If the board is full, display tie.
7. If neither player won and the board is not full, go to #2
8. Play again?
9. If yes, go to #1
10. Goodbye!
'''
# Display an Empty board
print('')
print('     |     |')
print('     |     |')
print('     |     |')
print('-----+-----+-----')
print('     |     |')
print('     |     |')
print('     |     |')
print('-----+-----+-----')
print('     |     |')
print('     |     |')
print('     |     |')
print('')

# Display board for an in-progress game

import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN_MATCH = 2
WHO_GOES_FIRST = 'Choose'
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
    [1, 5, 9], [3, 5, 7]             # diagonals
    ]

def display_board(board):
    os.system('clear')

    prompt(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

# Initialize a new board
def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items() if value == ' ']

def join_or(valid_choices, delimiter = ', ', joining_word = 'or'):
    if len(valid_choices) < 2:
        return delimiter.join(valid_choices)
    return f'{delimiter.join(valid_choices[:-1])}{delimiter}{joining_word} {valid_choices[-1]}'

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square

    return None

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square({join_or(valid_choices, ', ', 'or')}):")
        square = int(input().strip())
        if square in empty_squares(board):
            break

        prompt('Sorry, that is not a valid choice.')

    board[square] = HUMAN_MARKER # dictionary updated with user's input

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break

    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break

    if not square and board[5] == INITIAL_MARKER:
        square = 5

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        if all(board[sq] == HUMAN_MARKER for sq in line):
            return 'Player'
        if all(board[sq] == COMPUTER_MARKER for sq in line):
            return 'Computer'

    return None

def keep_score(board, score):
    game_winner = detect_winner(board)
    if game_winner == 'Computer':
        score['Computer'] += 1
    elif game_winner == 'Player':
        score['Player'] += 1

def match_winner(score):
    if score['Player'] == GAMES_TO_WIN_MATCH:
        prompt(f"Player has WON THE MATCH!")
        return True
    if score['Computer'] == GAMES_TO_WIN_MATCH:
        prompt(f"Computer has WON THE MATCH!")
        return True


def resolve_first_player():
    choice = WHO_GOES_FIRST.lower()
    if choice == 'choose':
        while True:
            prompt("Who goes first? (p / c)")
            answer = input().strip().lower()
            if answer in ('p', 'c'):
                return answer
            prompt("Enter 'p' or 'c'")
    elif choice in ('p', 'c'):
        return choice
    else:
        return 'p'

def choose_square(board, current_player):
    if current_player == 'p':
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def alternate_player(p):
    if p == 'p':
        return 'c'
    else:
        return 'p'

def play_tic_tac_toe():
    while True:
        score = {'Computer': 0, 'Player': 0}

        while score['Player'] < GAMES_TO_WIN_MATCH and score['Computer'] < GAMES_TO_WIN_MATCH:
            board = initialize_board()

            current_player = resolve_first_player()
            while True:
                display_board(board)
                choose_square(board, current_player)
                if someone_won(board) or board_full(board):
                    break
                current_player = alternate_player(current_player)

            display_board(board)

            if someone_won(board):
                prompt(f"{detect_winner(board)} won!")
            else:
                prompt("It's a tie!")

            keep_score(board, score)

            prompt(f"The match score is Player {score['Player']}:{score['Computer']} Computer")

            if match_winner(score):
                break

            while True:
                prompt("Press 'y' to start the next game.")
                answer = input().lower()
                if answer == 'y':
                    break
                prompt("Invalid: Enter 'y'")

        while True:
            prompt('Would you like to player another match? (y or n)')
            answer = input().lower()
            if answer in ('y', 'n'):
                break
            prompt("Enter a valid input: 'y' or 'n'")

        if answer == 'n':
            prompt('Thank you for playing tic-tac-toe.')
            break

play_tic_tac_toe()


