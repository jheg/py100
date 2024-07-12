# Tip Calculator
# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user will enter valid numbers.

# INPUT / OUTPUT
# Input: 
#   amount
#   rate
# Output:
#   tip
#   total 

# EXAMPLE
# [100.27, 10.0]
# The tip is £10,02
# The total is £110.29

# The inputs must be positive numeric values
# the outputs should have 2 decimal places

def process_bill():
    while True:
        bill_amount = float(input("please enter the bill amount: £ "))
        bill_confirmation = input(f"You entered £{bill_amount:.2f}. Is that correct? (Y to continue, N to re-enter): ")
        if bill_confirmation == "y".lower():
            break

    while True:
        tip_rate = float(input("Please enter the tip rate %: "))
        tip_confirmation = input(f"You entered {tip_rate:.2f}%. Is that correct? (Y to continue, N to re-enter): ")
        if tip_confirmation == "y".lower():
            break

    total_bill = bill_amount + (bill_amount * (tip_rate / 100))     

    print(f"The tip is £{bill_amount * (tip_rate / 100):.2f}")
    print(f"The total is £{total_bill:.2f}")

process_bill()