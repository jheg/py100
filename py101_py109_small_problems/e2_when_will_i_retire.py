"""
When Will I Retire?
Build a program that displays when the user will retire and how many years she has to work till retirement.
"""
from datetime import date

def retirement_calc():
    age = int(input('What is your age? '))
    intended_retirement = int(input('At what age do you (or did you) intend to retire? '))
    years_left = intended_retirement - age
    current_year = date.today().year

    if years_left < 0:
        return f"That's {abs(years_left)} year(s) ago, eek! :|"
    elif years_left == 0:
        return f"It's your retirement year, enjoy retirement!"
    else:
        return f"It's {current_year}. You will retire in {current_year + years_left}.\nYou have {years_left} years of work to go!"

print(retirement_calc())