from random import randrange

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i < int(num**(0.5))+1:
        if num % i == 0: return False
        i += 2
        if num % i == 0: return False
        i += 4
    return True

def row_exist(i, n, array):
    count = n
    for j in range(n):
        num = array[i][j]
        while num != 0:
            digit = num%10
            if is_prime(digit):
                count-=1#if one digit in current number is prime then count -= 1
                break
            num //= 10
    if count != 0: return False
    return True#count == 0 what means there is row where every number has at least one prime digit

def row_with_prime_digits(n):
    array = [[randrange(1, 37) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        print(array[i])

    for i in range(n):
        if row_exist(i, n, array): return True
    return False

if __name__ == '__main__':
    print(row_with_prime_digits(5))