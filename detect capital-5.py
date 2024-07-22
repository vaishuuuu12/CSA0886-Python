def is_proper_capital_usage(word):
    if word.isupper():
        return True
    elif word.islower():
        return True
    elif word[0].isupper() and word[1:].islower():
        return True
    else:
        return False

word1 = "USA"
word2 = "demo"
print(is_proper_capital_usage(word1))
print(is_proper_capital_usage(word2))
