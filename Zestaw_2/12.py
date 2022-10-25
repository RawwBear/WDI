import math

def get_leng(num):
    #we need to add 1 because it represents the unity digit
    return math.floor(math.log10(num)) + 1

def is_digit_equal_leng(num):
    leng = get_leng(num)
    while num != 0:
        if num%10 == leng:
            return True
        num //= 10
    return False

print(is_digit_equal_leng(125))
