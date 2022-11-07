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


def check_around(i, j, n, array):
    combination = [(1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (0, 1), (0, -1), (-1, 1)]
    primes = 0
    for x, y in combination:
        if i+x > n-1 or i+x < 0 or j+y > n-1 or j+y< 0:
            continue
        else:
            if is_prime(array[x+i][y+j]): primes += 1
    if primes > 2: return False
    return True



def six_neighbours(n):
    array = [[randrange(1, 31) for _ in range(n)]for _ in range(n)]
    for i in range(n):
        print(array[i])
    row_count = 0
    for j in range(n):#count elements with at least 6 composed neighbours in the first row
        row_count += check_around(0,j,n, array)
    count = 0
    for i in range(1, n):#start from second row
        for j in range(n):
            count += check_around(i, j, n, array)
        if count != row_count: return False
    return True

if __name__ == '__main__':
    print(six_neighbours(5))