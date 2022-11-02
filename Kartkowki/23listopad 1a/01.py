import math
def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3 or n == 5: return True
    if n%2== 0 or n%3==0 or n%5==0: return False
    i = 7
    while i <= int(n**0.5)+1:
        if n%i == 0: return False
        i += 2
    return True

def get_leng(n):
    return math.floor(math.log10(n)) + 1

def diff_digits(n):
    array = [False for _ in range(10)]
    while n!= 0:
        digit = n%10
        if array[digit] == True: return False
        array[digit] = True
        n //= 10
    return True

def biggest_num(k):
    #I can remove only first and last digits, we can't get non-continous sequence
    multi_m = 10 ** (get_leng(k) - 1)
    num = k
    biggest = 0
    for m in range(get_leng(k)):#remove first digits
        multi_n = 1
        for n in range(get_leng(num)):#remove last digits
            new_number = num // multi_n
            if is_prime(new_number):
                if diff_digits(new_number):
                    if new_number > biggest:
                        biggest = new_number
            multi_n *= 10
        num = k%multi_m
        multi_m //= 10
    return biggest

if __name__ == '__main__':
    print(biggest_num(1202742516))
    print(is_prime(74251))