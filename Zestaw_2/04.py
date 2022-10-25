def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    i = 5
    while i < int(num**(0.5))+1:
        if num % i == 0: return False
        i += 2
        if num % i == 0: return False
        i += 4

def how_many_235_nums(n):
    if n < 7:
        return n
    counter = 6 #in range(1,7) there is 6 such numbers
    for num in range(7, n+1):
        if is_prime(num) == True: continue#if number is prime and >5 then can't be dived only by 2,3,5
        while num%2 == 0:
            num //=2
        while num%3 == 0:
            num //= 3
        while num%5 == 0:
            num //= 5
        if num == 1:
            counter += 1
    return counter

if __name__ == '__main__':
    print(how_many_235_nums(122))