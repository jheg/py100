# X Ask the user for the capital & interest amount
# X Ask the user for the interest only amount
# X Ask the user for the interest rate
# X Ask the user for the term in years
# X Ask the user for the term in months (For terms that run over a whole yr)
# X Perform the calculation and output the result to the terminal
# X Build in validation to handle bad input
# X Tidy up display output
# Validate where years and months is not greater than 0

import math

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

def calculate(capital_and_interest, interest_only, rate, years, months):
    total_term = (years * 12) + months
    int_rate = rate / 100
    monthly_interest = int_rate / 12
    denominator = 1 - (1 + monthly_interest) ** (-total_term)

    cap_int_payment = capital_and_interest * ( monthly_interest / denominator)
    int_only_payment = (interest_only * int_rate) / 12

    monthly_payment = cap_int_payment + int_only_payment

    prompt('----------------------------------')
    prompt(f'Capital & Interest amount: £{float(capital_and_interest):,.2f}')
    prompt(f'Interest Only amount: £{float(interest_only):,.2f}')
    prompt(f'Interest Rate: {float(rate):,.2f}%')
    prompt(f'Term (Years): {years}')
    prompt(f'Term (Months): {months}')
    prompt('----------------------------------')
    prompt(f"{messages['result']}{float(monthly_payment):,.2f}")
    prompt('----------------------------------')

def get_capital_and_interest():
    prompt(messages['capint'])
    amount = input('£')

    while invalid_int(amount):
        prompt(messages['invalid_amount'])
        amount = input('£')

    return float(amount)

def get_interest_only():
    prompt(messages['intonly'])
    amount = input('£')

    while invalid_int(amount):
        prompt(messages['invalid_amount'])
        amount = input('£')

    return float(amount)

def get_interest_rate():
    prompt(messages['int_rate'])
    amount = input('Rate: ')

    while invalid_interest_rate(amount):
        prompt(messages['invalid_rate'])
        amount = input('Rate: ')

    return float(amount)

def get_years():
    prompt(messages['term_years'])
    years = input('Years: ')

    while invalid_term_years(years):
        prompt(messages['invalid_years'])
        years = input('Years: ')

    return int(years)

def get_months():
    prompt(messages['term_months'])
    months = input('Months: ')

    while invalid_term_months(months):
        prompt(messages['invalid_months'])
        months = input('Months: ')

    return int(months)

def invalid_int(num):
    try:
        int(num)
        if int(num) < 0:
            return True
    except (TypeError, ValueError):
        return True
    return False

def invalid_interest_rate(rate):
    try:
        rate_float = float(rate)
        if math.isinf(rate_float) or math.isnan(rate_float) or rate_float < 0:
            return True
    except (TypeError, ValueError):
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
cap_and_int = get_capital_and_interest()
int_only = get_interest_only()
interest_rate = get_interest_rate()
term_years = get_years()
term_months = get_months()

calculate(
    cap_and_int,
    int_only,
    interest_rate,
    term_years,
    term_months)