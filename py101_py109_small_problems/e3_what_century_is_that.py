"""
What Century is That?

Write a function that takes a year as input and returns the century. 
The return value should be a string that begins with the century number, 
and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

0           =>      1st
1           =>      1st

11          =>      1st
12          =>      1st

101         =>      2nd
101         =>      2nd

1001        =>      11th
1002        =>      11th
1003        =>      11th

10001       =>      101st
10002       =>      101st

100001      =>      1001st
100002      =>      1001st

1000001     =>      10001st
1000002     =>      10001st

1           =>      1st
3           =>      3rd
11          =>      11th
12          =>      12th
20          =>      20th
20          =>      20th
21          =>      21st
102         =>      102nd
113         =>      113th
"""

def century(year):
    century_number = year // 100 + 1

    if year % 100 == 0:
        century_number -= 1

    suffix = century_suffix(century_number)
    return f'{century_number}{suffix}'

def century_suffix(century_number):
    last_two_digits = century_number % 100
    last_digit = century_number % 10

    match last_two_digits:
        case 11|12|13:
            return 'th'
            
    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'    

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True