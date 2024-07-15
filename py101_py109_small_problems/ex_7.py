"""
Short Long Short

Write a function that takes two strings as arguments, determines the length of the two strings, 
and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. 
You may assume that the strings are of different lengths.
"""

def short_long_short(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        return f"{str2}{str1}{str2}"
    else:
        return f"{str1}{str2}{str1}"

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")