import random

deck = [
    '2','2','2','2',
    '3','3','3','3',
    '4','4','4','4',
    '5','5','5','5',
    '6','6','6','6',
    '7','7','7','7',
    '8','8','8','8',
    '9','9','9','9',
    '10','10','10','10',
    'Jack','Jack','Jack','Jack',
    'Queen','Queen','Queen','Queen',
    'King','King','King','King',
    'Ace','Ace','Ace','Ace'
]
# Excluding Ace values as they will be handled in their own function. By default, 'Ace' has a value of 11
CARD_VALUES = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10,
    'Ace' : 1
}

def update_score(card, score):
    if card == 'Ace' and score < 11:
        card_value = 11
    else:
        card_value = CARD_VALUES[card]
    return card_value

def initial_hand(deck):
    hand = [random.choice(deck), random.choice(deck)]

    for card in hand:
        deck.remove(card)

    return hand

def check_bust(score):
    if score > 21:
        return True

def play_21():
    player_score = 0
    dealer_score = 0
    player_hand = initial_hand(deck)
    dealer_hand = initial_hand(deck)

    print(player_hand)
    print(dealer_hand)

    for card in player_hand:
        player_score += update_score(card, player_score)
        print(player_score)
    for card in dealer_hand:
        dealer_score += update_score(card, dealer_score)
    print(f'Your score is {player_score}.')
    print(f"One of the dealer's card is {random.choice(dealer_hand)}")

    while True:
        while True:
            print(f'Would you like to hit or stay? (h/s)')
            answer = input()
            if answer == 'h':
                card = random.choice(deck)
                deck.remove(card)
                player_score += update_score(card, player_score)
                print(f'Your score is {player_score}.')
            elif answer == 's':
                break
            if check_bust(player_score):
                print('You have gone bust!')
                print('Dealer wins.')
                break

        if check_bust(player_score):
            break

        while True:
            print(dealer_score)
            if dealer_score < 17:
                card = random.choice(deck)
                deck.remove(card)
                dealer_score += update_score(card, dealer_score)
            else:
                break

        if check_bust(dealer_score):
            print('Dealer went bust!')
            print('Player wins.')
            break
        elif dealer_score > player_score:
            print('Dealer wins!')
            break
        elif player_score > dealer_score:
            print('Player wins!')
        else:
            print("It's a tie.")
            break

play_21()








