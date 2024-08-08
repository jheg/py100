import random
import time

VALID_CHOICES = {
    '1': 'rock',
    '2': 'paper',
    '3': 'scissors',
    '4': 'lizard',
    '5': 'spock'
}

WINNING_COMBOS = {
    'rock': {
        'lizard': 'crushes',
        'scissors': 'crushes',
        },
    'paper': {
        'rock': 'covers',
        'spock': 'disproves',
        },
    'scissors': {
        'paper': 'cuts',
        'lizard': 'decapitates',
        },
    'lizard': {
        'paper': 'eats',
        'spock': 'poisons',
        },
    'spock': {
        'scissors': 'smashes',
        'rock': 'vaporizes',
        }
}
WELCOME = """
Welcome to Rock, Paper, Scissors, Lizard, Spock.

Options: 
1 => Rock (crushes lizard & scissors)
2 => Paper (covers rock & disproves spock)
3 => Scissors (cuts paper & decapitates lizard)
4 => Lizard (eats paper & poisons spock)
5 => Spock (smashes scissors & vaporizes rock)

Best of 5, good luck!
"""
MESSAGES = {
    "choose":               "Enter your choice:",
    "winner":               "You win!",
    "lose":                 "You lose",
    "tie":                  "It's a tie\n",
    "end_winner":           "You are the winner!",
    "end_loser":            "Game over, you lose.",
    "play_again":           "Play again? (y/n)"
}

formatted_choices = [
    f"{value} ({key})" for key, value in VALID_CHOICES.items()
]

def invalid_choice(choice):
    if choice not in VALID_CHOICES.keys():
        return True
    return False

def prompt(msg):
    print(f"==> {msg}")

def update_score(number):
    return number + 1

def player_wins(player_1_choice, player_2_choice):
    return player_2_choice in WINNING_COMBOS[player_1_choice].keys()

def display_outcome(winner, loser):
    prompt(f'Outcome:{" " * 12}{VALID_CHOICES[winner]} '
           f'{WINNING_COMBOS[VALID_CHOICES[winner]][VALID_CHOICES[loser]]} '
           f'{VALID_CHOICES[loser]}\n')

while True:
    prompt(WELCOME)

    player_1_score = 0
    player_2_score = 0
    game_round = 1

    while True:
        time.sleep(1)
        prompt(f'Round {game_round}')
        if game_round > 1:
            prompt(f"Player 1 score: {player_1_score}")
            prompt(f"Computer score: {player_2_score}\n")

        prompt(MESSAGES["choose"])
        player_choice = input()
        computer_choice = random.choice(list(VALID_CHOICES.keys()))

        while invalid_choice(player_choice):
            prompt(f'Please select from the following: '
                    f'{", ".join(formatted_choices)}')
            player_choice = input('Enter your choice: ')

        player_choice_string = VALID_CHOICES[player_choice]
        computer_choice_string = VALID_CHOICES[computer_choice]

        prompt(f'You: {" " * 15}{player_choice_string.capitalize()}')
        prompt(f'Computer: {" " * 10}{computer_choice_string.capitalize()}')

        if player_wins(player_choice_string, computer_choice_string):
            player_1_score = update_score(player_1_score)
            prompt(f'Result:{" " * 13}{MESSAGES["winner"]}')
            display_outcome(player_choice, computer_choice)
        elif player_wins(computer_choice_string, player_choice_string):
            player_2_score = update_score(player_2_score)
            prompt(f'Result:{" " * 13}{MESSAGES["lose"]}')
            display_outcome(computer_choice, player_choice)
        else:
            prompt(f'Result:{" " * 13}{MESSAGES["tie"]}')

        game_round += 1

        if player_1_score == 3:
            prompt(MESSAGES["end_winner"])
            break
        if player_2_score == 3:
            prompt(MESSAGES["end_loser"])
            break

    prompt(MESSAGES['play_again'])
    play_again = input()
    if play_again == 'n':
        break