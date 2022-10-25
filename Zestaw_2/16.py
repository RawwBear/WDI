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

def digit_sum(num):
    count = 0
    if num < 10:
        return num
    else:
        while num!=0:
            count += num%10
            num //= 10
        return count

def smith_numbers(n=1000_000):
    for number in range(4, n):
        if is_prime(number) == True:
            continue
        num = number
        factors_sum = 0
        i = 2
        while num != 1:
            while num%i == 0:
                factors_sum += i
                num //= i
            if is_prime(num) == True:
                factors_sum += digit_sum(num)
                num = 1
            i += 1
        if factors_sum == digit_sum(number):
            print(number)

print(smith_numbers(1000))
