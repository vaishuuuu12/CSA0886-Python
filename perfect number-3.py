def is_perfect_number(n):
    if n <= 1:
        return False
    sum_of_divisors = 1
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
    return sum_of_divisors == n
n = 28
print(is_perfect_number(n)) 
