def is_ascending_seq(num):
    if num > 9:
        while num != 0:
            last_digit = num%10
            num //= 10
            pre_last = num%10
            if last_digit <= pre_last:
                return False
            num //= 10
    return True

print(is_ascending_seq(17234))