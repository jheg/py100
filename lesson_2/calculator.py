# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Print the result to the terminal.
# X Perform the operation on the two numbers.
# X Ask the user if they want to run another calculation.
# X Extract messages into separate json file

import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(data['welcome'])
end_calculator = True

while end_calculator:
    prompt(data['1st'])
    number1 = input()

    while invalid_number(number1):
        prompt(data['invalid'])
        number1 = input()

    prompt(data['2nd'])
    number2 = input()

    while invalid_number(number2):
        prompt(data['invalid'])
        number2 = input()

    prompt(data['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3 or 4')
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f'The result is: {output}')
    prompt(data['again'])

    end_calculator = input()

    if end_calculator == '':
        prompt(data['bye'])