# LBYL: Look Before You Leap (Uses guard clauses)
def lower_word(word):
    if isinstance(word, str) != True:
        return word

    if len(word) == 0:
        return word

    return word[0].lower() + word[1:]

print(lower_word("FOO"))
print(lower_word(95))
print(lower_word(""))

# EAFP: It's Easier to Ask Forgiveness than Permission
def lower_first(word):
    try:
        word = word.strip()
        return word[0].lower() + word[1:]
    except (TypeError, IndexError, AttributeError):
        return word

print(lower_first("FOO"))
print(lower_first(" FOO"))
print(lower_first(57))
print(lower_first(""))