from random import randrange

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3 or num == 5:
        return True
    if num%2 == 0 or num%3 == 0 or num%5 == 0:
        return False
    i = 7
    while i < int(num**0.5):
        if num%i == 0:
            return False
        i += 2
    return True

def condition(n):
    f1, f2 = 1, 1
    array = [randrange(1, 101) for _ in range(n)]
    flag = False
    for idx, num in enumerate(array):
        if idx > f1:
            f1, f2 = f2, f1 + f2
        if idx == f1:
            # print(idx, f1)
            if is_prime(num) == True or num < 1:
                return False
        else:
            if is_prime(num):
                flag = True
    if flag == True:
        return True

if __name__ == '__main__':
    print(condition(20))
    # print(is_prime(73))