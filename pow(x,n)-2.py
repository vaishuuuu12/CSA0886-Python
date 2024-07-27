x = 2.00000
n = 10
if n == 0:
    result = 1.0
else:
    if n < 0:
        x = 1 / x
        n = -n
    result = 1.0
    current_product = x
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2
print(result)
