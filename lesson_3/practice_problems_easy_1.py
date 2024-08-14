# Exercise 2
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def ends_with(text, char):
    if text[-1] == char:        # solutiuon used text.endswith('!')
        print(True)
    else:
        print(False)

ends_with(str1, "!")
ends_with(str2, "!")

# Exercise 3
famous_words = "seven years ago..."
new_string = "Four score and " + famous_words
new_string_2 = f'Four score and {famous_words}'
print(new_string)
print(new_string_2)

# Exercise 4
# Using the following string, print a string that contains the same value, 
# but using all lowercase letters except for the first character, 
# which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

print(munsters_description.capitalize())

# Exercise 5
# Swap case of all letters
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())

# Exercise 6
# Determine whether the name Dino appears in the strings below -- 
# check each string separately:

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print("Dino" in str1)
print("Dino" in str2)

# Exercise 7
# How can we add the family pet, "Dino", to the following list?

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
print(flintstones)

# Exercise 8
# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.

flintstones.extend(['Dino', 'Hoppy'])
print(flintstones)

# Exercise 9
# Print a new version of the sentence given by advice that ends 
# just before the word house. Don't worry about spaces or punctuation: 
# remove everything starting from the beginning of 
# house to the end of the sentence.

advice = "Few things in life are as important as house "
"training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice[0:advice.find('house')])
print(advice.split("house")[0])         # creates a list up to 'house' and 
                                        # returns element at index 0 

# Exercise 10
# Print the following string with the word important replaced by urgent:
advice = "Few things in life are as important as house "
"training your pet dinosaur."
new_advice = advice.split('important')
# print(new_advice)
    # print(advice.find('important'))
# new_advice[6] = 'urgent'
print(f"{'urgent'.join(new_advice)}")

advice = advice.replace('important', 'urgent')
print(advice)