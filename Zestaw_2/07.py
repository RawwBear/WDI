def is_multiple_exp(num):
    a = 3
    diff = 4
    while num >= a:
        if num % a == 0:
            return True
        a += diff
        diff += 2
    return False

if __name__ == '__main__':
    print(is_multiple_exp(33))