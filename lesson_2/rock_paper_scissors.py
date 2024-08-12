import random
import time
import os

VALID_CHOICES = {
    '1': 'rock',
    '2': 'paper',
    '3': 'scissors',
    '4': 'lizard',
    '5': 'spock'
}

formatted_choices = [
    f"{value} ({key})" for key, value in VALID_CHOICES.items()
]

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

MESSAGES = {
    "choose":               "Enter your choice:",
    "winner":               "You win!",
    "lose":                 "You lose",
    "tie":                  "It's a tie\n",
    "end_winner":           "You are the winner!",
    "end_loser":            "Game over, you lose.",
    "play_again":           "Play again? (y/n)",
    "end_game":             "Goodbye, thanks for playing."
}

def clear_screen():
    # clear screen based on operating system
    os.system('cls' if os.name == 'nt' else 'clear' )

def wait(num):
    time.sleep(num)

def prompt(msg):
    print(f"==> {msg}")

def display_welcome_message():
    print("""Welcome to Rock, Paper, Scissors, Lizard, Spock.

Options: 
1 => Rock (crushes lizard & scissors)
2 => Paper (covers rock & disproves spock)
3 => Scissors (cuts paper & decapitates lizard)
4 => Lizard (eats paper & poisons spock)
5 => Spock (smashes scissors & vaporizes rock)

Best of 5, good luck!
""")

def prompt_player_choice():
    prompt(MESSAGES["choose"])
    player_choice = input()

    while invalid_choice(player_choice):
        prompt(f'Please select from the following: '
                f'{", ".join(formatted_choices)}')
        player_choice = input('Enter your choice: ')

    return VALID_CHOICES[player_choice]

def invalid_choice(choice):
    if choice not in list(VALID_CHOICES):
        return True
    return False

def get_computer_choice():
    return random.choice(list(WINNING_COMBOS))

def display_choices(player_choice_string, computer_choice_string):
    prompt(f'You: {" " * 15}{player_choice_string.capitalize()}')
    prompt(f'Computer: {" " * 10}{computer_choice_string.capitalize()}')

def player_wins(player_1_choice, player_2_choice):
    return player_2_choice in list(WINNING_COMBOS[player_1_choice])

def get_winner(player, computer):
    if player_wins(player, computer):
        winner = "you"
        return winner
    if player_wins(computer, player):
        winner = "computer"
        return winner

    return False

def display_scoreboard(scoreboard):
    if scoreboard["game_round"] > 0:
        prompt(f'Round {scoreboard["game_round"]}')
        prompt(f'Your score: {scoreboard["you"]}')
        prompt(f'Computer score: {scoreboard["computer"]}\n')

def update_scoreboard(scoreboard, round_winner):
        if round_winner:
            scoreboard[round_winner] += 1
        scoreboard["game_round"] += 1

def display_result(round_winner):
    if round_winner == "you":
        prompt(f'Result:{" " * 13}{MESSAGES["winner"]}')
    elif round_winner == "computer":
        prompt(f'Result:{" " * 13}{MESSAGES["lose"]}')
    else:
        prompt(f'Result:{" " * 13}{MESSAGES["tie"]}')

def display_outcome(player_choice, computer_choice, round_winner):
    match round_winner:
        case False:
            return False
        case "you":
            prompt(f'Outcome:{" " * 12}{player_choice} '
                f'{WINNING_COMBOS[player_choice][computer_choice]} '
                f'{computer_choice}')
        case "computer":
            prompt(f'Outcome:{" " * 12}{computer_choice} '
                f'{WINNING_COMBOS[computer_choice][player_choice]} '
                f'{player_choice}')

def display_round_summary(player_choice, computer_choice, round_winner):
    display_choices(player_choice, computer_choice)
    display_outcome(player_choice, computer_choice, round_winner)
    display_result(round_winner)

def game_over_check(scoreboard):
    game_over = False
    if scoreboard["you"] == 3:
        prompt(MESSAGES["end_winner"])
        game_over = True
        return game_over
    if scoreboard["computer"] == 3:
        prompt(MESSAGES["end_loser"])
        game_over = True
        return game_over

    return game_over

def play_again():
    prompt(MESSAGES['play_again'])
    user_response = input()
    if user_response == 'n':
        prompt(MESSAGES["end_game"])
        return False
    return True

def main_game():
    while True:
        scoreboard = {
            "you": 0,
            "computer": 0,
            "game_round": 1
        }
        clear_screen()
        display_welcome_message()

        while True:
            display_scoreboard(scoreboard)
            player_choice = prompt_player_choice()
            computer_choice = get_computer_choice()
            round_winner = get_winner(player_choice, computer_choice)
            update_scoreboard(scoreboard, round_winner)
            display_round_summary(player_choice, computer_choice, round_winner)
            wait(2)
            clear_screen()
            if game_over_check(scoreboard):
                break

        if play_again() is False:
            break

main_game()