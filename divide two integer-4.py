def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is undefined")
    if dividend == 0:
        return 0
    negative = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            quotient += i
            i <<= 1
            temp <<= 1
    if negative:
        quotient = -quotient
    return max(-2*31, min(2*31 - 1, quotient))
dividend1 = 10
divisor1 = 3
print(divide(dividend1, divisor1))
