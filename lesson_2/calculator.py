# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Print the result to the terminal.
# X Perform the operation on the two numbers.
# Ask the user if they want to run another calculation.


def prompt(message):
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')
end_calculator = True

while end_calculator:
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    prompt("What operation would you liek to perform?\n"
        "1) Add 2) Subtract 3) Multiply 4) Divide")
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
    prompt("Do you want to run another calculation?\n"
           "To EXIT press Enter\n"
           "To run another calculation press any key + Enter\n")
           
    end_calculator = input()

    if end_calculator == '':
        prompt('Goodbye.\n')