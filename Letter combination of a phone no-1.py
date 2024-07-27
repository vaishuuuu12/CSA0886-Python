digits = "23"
digit_to_letters = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
}
combinations = [""] if digits else []
for digit in digits:
    combinations = [prefix + letter for prefix in combinations for letter in digit_to_letters[digit]]
print(combinations)
