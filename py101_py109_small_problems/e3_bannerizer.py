"""
Bannerizer
Write a function that takes a short line of text and prints it within a box.
"""
def print_in_box(str):
    top_bottom_border = f'+{(len(str) + 2) * "-"}+'
    empty_line = f'|{(len(str) + 2) * " "}|'
    msg = f'| {str} |'

    print(top_bottom_border)
    print(empty_line)
    print(msg)
    print(empty_line)
    print(top_bottom_border)


def print_truncated(str, num):
    top_bottom_border = f'+{num * "-"}+'
    empty_line = f'|{num * " "}|'
    msg = f'| {str[0:num - 5]}... |'
    
    print(top_bottom_border)
    print(empty_line)
    print(msg)
    print(empty_line)
    print(top_bottom_border)


def print_wrapped(str, num):
    str_length = len(str)

    top_bottom_border = f'+--{num * "-"}--+'
    empty_line = f'|  {num * " "}  |'

    msgs = []
    current_start_index = 0

    while current_start_index <= str_length:
        if num - len(str[current_start_index:-1]) < 0:
            remainder = 1
            msgs.append(f'| {(remainder * " ") + str[current_start_index:current_start_index+num] + (remainder * " ")} |')
        else:
            remainder = num - len(str[current_start_index:-1])
            msgs.append(f'|  {str[current_start_index:-1] + (remainder * " ")}  |')
        
        current_start_index += num
        

    print(top_bottom_border)
    print(empty_line)
    for split in msgs:
        print(split)
    print(empty_line)
    print(top_bottom_border)


def output_choice(str, num=0):
    str_length = len(str)
    if num and str_length <= num:
        print_in_box(str)
    elif num and str_length > num:
        choice = input('Enter any character to Truncate or Enter to wrap. ')
        if choice:
            print('\nHere is your truncated message...')
            print_truncated(str, num)
        else:
            print('\nHere is your wrapped message...')
            print_wrapped(str,num)
    else:
        print_in_box(str)

output_choice('To boldly go where no one has gone before.', 40)
output_choice('To boldly go where no one has gone before.', 20)
output_choice('To boldly go where no one has gone before.', 10)
output_choice('To boldly go where no one has gone before.')
output_choice('')