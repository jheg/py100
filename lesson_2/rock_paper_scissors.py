"""
Both opponents choose an item from rock, paper, or scissors. The winner is 
decided according to the following rules:

If player a chooses rock and player b chooses scissors, player a wins.
If player a chooses paper and player b chooses rock, player a wins.
If player a chooses scissors and player b chooses paper, player a wins.
If both players choose the same item, neither player wins. It's a tie.
Our version of the game lets the user play against the computer. The game flow 
should go like this:

The user makes a choice.
The computer makes a choice.
The winner is displayed.
"""
# X Extract messages to a dictionary
# X Simplify input choices with a single key input from ['1','2','3']
# Build function to check high score
# Calculate len of longest message in order to wrap game in a border frame
# Allow 2 player game
# X Build best of 5
# X Extend with Spock and Lizard options
# Extract high scores out of game session rock_paper_scissors_high_scores.py

import random

VALID_CHOICES = {
    '1': 'Rock',
    '2': 'Paper',
    '3': 'Scissors',
    '4': 'Lizard',
    '5': 'Spock'
}
formatted_choices = [f"{value} ({key})" for key, value in VALID_CHOICES.items()]

def invalid_choice(choice):
    if choice not in VALID_CHOICES:
        return True
    return False

def prompt(msg):
    print(f"==> {msg}")

messages = {
    "border":               "+----------------------------------+",
    "welcome":              "| Welcome to Rock, Paper, Scissors",
    "intro":                "| Best of 5",
    "new_high_score":       "| NEW HIGH SCORE",
    "winner":               "You win!",
    "lose":                 "You lose",
    "tie":                  "It's a tie",
    "play_again":           "Play again? (y/n)"
}

def update_score(number):
    return number + 1

def get_winner(player_1_choice, player_2_choice):
    match player_1_choice:
        case '1':
            if player_2_choice in ['3', '4']:
                return 'player_1'
            if player_2_choice in ['2', '5']:
                return 'player_2'
        case '2':
            if player_2_choice in ['1', '5']:
                return 'player_1'
            if player_2_choice in ['3', '4']:
                return 'player_2'
        case '3':
            if player_2_choice in ['2', '4']:
                return 'player_1'
            if player_2_choice in ['1', '5']:
                return 'player_2'
        case '4':
            if player_2_choice in ['2', '5']:
                return 'player_1'
            if player_2_choice in ['1', '3']:
                return 'player_2'
        case '5':
            if player_2_choice in ['1', '3']:
                return 'player_1'
            if player_2_choice in ['2', '4']:
                return 'player_2'

    return 'tie'

while True:
    prompt(messages['border'])
    prompt(messages['welcome'])
    prompt(messages['intro'])
    prompt(messages['border'])

    player_1_score = 0
    player_2_score = 0

    while True:
        # prompt(f'| Highest Win Streak: {highest_win_streak}')
        print(f"Player 1 score: {player_1_score}")
        print(f"Player 2 score: {player_2_score}")
        prompt('')

        prompt(f'| Choose: {", ".join(formatted_choices)}')
        player_choice = input('Enter your choice: ')
        computer_choice = random.choice(list(VALID_CHOICES.keys()))
        prompt('')

        while invalid_choice(player_choice):
            prompt(f'| Please select from the following: '
                    f'{", ".join(formatted_choices)}')
            player_choice = input('Enter your choice: ')
            prompt('')

        prompt(f'| Your choice: {VALID_CHOICES[player_choice]}')
        prompt(f'| Computers choice: {VALID_CHOICES[computer_choice]}')

        get_winner(player_choice, computer_choice)

        if get_winner(player_choice, computer_choice) == 'player_1':
            prompt(f'WINNER {VALID_CHOICES[player_choice]} '
                   f'beats {VALID_CHOICES[computer_choice]}')
            player_1_score = update_score(player_1_score)
        elif get_winner(player_choice, computer_choice) == 'player_2':
            prompt(f'LOSER {VALID_CHOICES[computer_choice]} '
                   f'beats {VALID_CHOICES[player_choice]}')
            player_2_score = update_score(player_2_score)
        else:
            prompt("It's a tie")

        prompt('')

        if player_1_score == 3:
            prompt('You are the winner!')
            break
        if player_2_score == 3:
            prompt('Game over, you lose.')
            break

    prompt(messages['play_again'])
    play_again = input()
    if play_again == 'n':
        break