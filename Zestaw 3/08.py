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

def start_to_end(size, n):
    array = [randrange(1, 1001) for _ in range(size)]
    # array = [24, 25,80, 49, 78]
    k = 0
    while array[k]%n == 0 and is_prime(n) and k < len(array)-1:
        k += n
        if k > len(array)-1:
            return False
    if k == len(array)-1:
        return True
    return False

def zero_to_end(t:[]):
    array = [False for _ in range(len(t))]
    array[0] = True
    for k in range(len(t)):
        if array[k]:
            temp = t[k]
            i = 2
            while temp != 1:
                while temp%i == 0:
                    if k + i < len(t):
                        array[k + i] = True
                    temp //= i
                i += 1
    return array[len(t)-1]

if __name__ == '__main__':
    print(start_to_end(10,2))
    print(zero_to_end([6, 1, 5, 2, 4, 3, 9, 9, 1, 2, 4]))#True
