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

def number_with_prime_only_digits(num):
    while num != 0:
        digit = num%10
        if is_prime(digit) == False:
            return False
        num //= 10
    return True

def row_with_prime_digits(n):
    array = [[randrange(1, 37) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        print(array[i])

    for i in range(n):
        flag = False
        for j in range(n):
             if number_with_prime_only_digits(array[i][j]):
                flag = True
                break
        if flag == False:return False
    return True

if __name__ == '__main__':
    print(row_with_prime_digits(5))