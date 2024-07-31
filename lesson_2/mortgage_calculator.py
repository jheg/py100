# X Ask the user for the capital & interest amount
# X Ask the user for the interest only amount
# X Ask the user for the interest rate
# X Ask the user for the term in years
# X Ask the user for the term in months (For terms that run over a whole yr)
# X Perform the calculation and output the result to the terminal
# X Build in validation to handle bad input
# X Tidy up display output

def prompt(msg):
    print(f"=> {msg}")

messages = {
    "top": "-----------------------------------------------------------------",
    "welcome": "Welcome to Mortgage Calculator\n",
    "about": "The calculator accepts:\n"
             "=>    Repayment mortgages,\n"
             "=>    Interest Only mortgages\n"
             "=>    Part Repayment / Part Interest Only mortgages\n",
    "capint": "Please enter the 'Repayment' amount",
    "intonly": "Please enter the 'interest only' amount",
    "term_years": "What is term in years and months?",
    "term_months": "What is term in years and months?",
    "int_rate": "What is the interest rate?",
    "result": "Monthly Payment: £",
    "invalid_amount": "Please enter a value containing only whole numbers, "
                      "for example 100000",
    "invalid_rate": "Please enter the interest rate as a numeric value, for "
                    "example, 3.45",
    "invalid_years": "Please enter a whole number greater than 0, for "
                     "example, 25",
    "invalid_months": "Please enter a whole number between 0 and 11, for "
                      "example 0",
}

def calculate():
    total_term = (int(term_years) * 12) + int(term_months)
    c_and_i = float(capital_and_interest)
    io = float(interest_only)
    rate = float(interest_rate) / 100
    monthly_interest = rate / 12
    denominator = 1 - (1 + monthly_interest) ** (-total_term)

    c_and_i_payment = c_and_i * ( monthly_interest / denominator)
    io_payment = (io * rate) / 12

    monthly_payment = c_and_i_payment + io_payment

    prompt('----------------------------------')
    prompt(f'Capital & Interest amount: £{float(c_and_i):,.2f}')
    prompt(f'Interest Only amount: £{float(io):,.2f}')
    prompt(f'Interest Rate: {float(interest_rate):,.2f}%')
    prompt(f'Term (Years): {int(term_years)}')
    prompt(f'Term (Months): {int(term_months)}')
    prompt('----------------------------------')
    prompt(f"{messages['result']}{float(monthly_payment):,.2f}")
    prompt('----------------------------------')


def invalid_int(num):
    try:
        int(num)
    except (TypeError, ValueError):
        return True
    return False

def invalid_interest_rate(rate):
    try:
        float(rate)
    except ValueError:
        return True
    return False

def invalid_term_years(term):
    try:
        int(term)
        if int(term) < 1:
            return True
    except (TypeError, ValueError):
        return True
    return False

def invalid_term_months(months):
    try:
        int(months)
        if int(months) not in range(0,12):
            return True
    except(TypeError, ValueError):
        return True 
    return False

prompt(messages['top'])
prompt(messages['welcome'])
prompt(messages['about'])

prompt(messages['capint'])
capital_and_interest = input('£')

while invalid_int(capital_and_interest):
    prompt(messages['invalid_amount'])
    capital_and_interest = input('£')

prompt(messages['intonly'])
interest_only = input('£')

while invalid_int(interest_only):
    prompt(messages['invalid_amount'])
    interest_only = input('£')

prompt(messages['int_rate'])
interest_rate = input('Rate: ')

while invalid_interest_rate(interest_rate):
    prompt(messages['invalid_rate'])
    interest_rate = input('Rate: ')

prompt(messages['term_years'])
term_years = input('Years: ')

while invalid_term_years(term_years):
    prompt(messages['invalid_years'])
    term_years = input('Years: ')

prompt(messages['term_months'])
term_months = input('Months: ')

while invalid_term_months(term_months):
    prompt(messages['invalid_months'])
    term_months = input('Months: ')



calculate()