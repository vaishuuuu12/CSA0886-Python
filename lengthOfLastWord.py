def lengthOfLastWord(s):
    words = s.strip().split()
    return len(words[-1]) if words else 0
s = "Hello World"
print(f"The length of the last word in '{s}' is: {lengthOfLastWord(s)}")

