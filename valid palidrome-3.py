def isPalindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    return normalized_str == normalized_str[::-1]
s1 = "A man, a plan, a canal: Panama"
print(f"Is the phrase '{s1}' a palindrome? {isPalindrome(s1)}")

