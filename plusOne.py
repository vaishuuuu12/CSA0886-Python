def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
digits = [1, 2, 3]
print(f"The result of incrementing {digits} is: {plusOne(digits)}")
