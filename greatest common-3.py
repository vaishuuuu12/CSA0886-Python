def gcd_of_strings(str1, str2):
    def divides(s, t):
        if len(s) % len(t) != 0:
            return False
        return s == t * (len(s) // len(t))
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    gcd_length = gcd(len(str1), len(str2))
    candidate = str1[:gcd_length]
    if divides(str1, candidate) and divides(str2, candidate):
        return candidate
    else:
        return ""
str1 = "ABABAB"
str2 = "ABAB"
print(gcd_of_strings(str1, str2))
