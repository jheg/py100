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

print(new_string)