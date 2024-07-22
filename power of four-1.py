def is_power_of_four(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0 and (n - 1) % 3 == 0
print(is_power_of_four(16)) 
