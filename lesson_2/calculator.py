# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Print the result to the terminal.
# X Perform the operation on the two numbers.
# X Ask the user if they want to run another calculation.
# X Extract messages into separate json file
# X Internationalise messages
# X Allow floating point numbers

import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt('Please choose your language, English (en) or Spanish (es)')
language = input()

prompt(data[language]['welcome'])
end_calculator = True

while end_calculator:

    prompt(data[language]['1st'])
    number1 = input()

    while invalid_number(number1):
        prompt(data[language]['invalid'])
        number1 = input()

    prompt(data[language]['2nd'])
    number2 = input()

    while invalid_number(number2):
        prompt(data[language]['invalid'])
        number2 = input()

    prompt(data[language]['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3 or 4')
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt(f"{data[language]['result']}{output}")
    prompt(data[language]['again'])
    end_calculator = input()


    if end_calculator == '':
        prompt(data[language]['bye'])