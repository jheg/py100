"""
The End Is Near But Not Here
Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.
"""

def penultimate(string):
    return string.split()[-2]

def middle(string):
    if type(string) is str:
        words = string.split()
    else: 
        return f'This gig only permits spaghetti you entered a {type(string)} datatype.'
    if len(words) <= 1:
        return f'You entered too few words {len(words)}. Please enter at least 3 words'
    elif len(words) % 2 == 0:
        return f'There is no middle here you entered an even number of words {len(words)}'
    else: 
        target_word = (len(words) // 2)
        return f'The middle word is "{words[target_word]}"'    



# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")


print(middle(500))                                      # This gig only permits spaghetti you entered a <class 'int'> datatype.
print(middle(['Jason', 'Lee', 'Hegarty']))              # This gig only permits spaghetti you entered a <class 'list'> datatype.
print(middle("Launch"))                                 # You entered too few words 1. Please enter at least 3 words
print(middle("Launch School is great!"))                # There is no middle here you entered an even number of words 4
print(middle("Launch School really is great!"))         # The middle word is "really"