def calculate_positive_difference(num1, num2):
    return abs(num1 - num2)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
positive_difference = calculate_positive_difference(num1, num2)
print(f"The positive difference between {num1} and {num2} is: {positive_difference}")
