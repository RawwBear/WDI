def is_last_digit_unique(num):
    last = num%10
    num //=10
    while num!= 0:
        if last == num%10:
            return False
        num //= 10
    return True

print(is_last_digit_unique(1234180))