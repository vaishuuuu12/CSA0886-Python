def is_perfect_square(num: int) -> bool:
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False
print(is_perfect_square(16))
