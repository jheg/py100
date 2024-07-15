"""
Leap Years (Part 2)
In the previous exercise, we assumed that the Gregorian calendar has been in continuous use since the year 1. 
However, the Gregorian calendar wasn't adopted until much later; prior to that, much of the world used the Julian calendar, 
which observed leap year every 4 years.

in 1752, England, Ireland, and the British colonies all switched to the Gregorian calendar. 
Update the function from the previous exercise so it uses the Julian calendar prior to 1752, and the Gregorian calendar starting in 1752.

=> Create a dictionary of when the Gregorian calander was adopted by country
=> Determine which calander to implement Gregorian or Julian
"""
gregorian_adoption = {
    "ES": 1582,
    "PT": 1582,
    "FR": 1582,
    "IT": 1582,
    "GB": 1752,
    "SE": 1753,
    "JP": 1873
}

def is_leap_year(country_code, year):
    if year < gregorian_adoption[country_code] and year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

# These examples should all print True
print(is_leap_year('GB', 1) == False)
print(is_leap_year('GB', 2) == False)
print(is_leap_year('GB', 3) == False)
print(is_leap_year('GB', 4) == True)
print(is_leap_year('GB', 1000) == True)
print(is_leap_year('GB', 1100) == True)
print(is_leap_year('GB', 1200) == True)
print(is_leap_year('GB', 1300) == True)
print(is_leap_year('GB', 1751) == False)
print(is_leap_year('GB', 1752) == True)
print(is_leap_year('GB', 1753) == False)
print(is_leap_year('GB', 1800) == False)
print(is_leap_year('GB', 1900) == False)
print(is_leap_year('GB', 2000) == True)
print(is_leap_year('GB', 2023) == False)
print(is_leap_year('GB', 2024) == True)
print(is_leap_year('GB', 2025) == False)