from random import randrange

n = int(input("Enter size of the arrays: "))
arr1, arr2 = [randrange(1, 11) for _ in range(n)], [randrange(1, 11) for _ in range(n)]

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

def generate_totals(mask:int):
    total = 0
    for i in range(n):
        if mask%3 == 0:
            total += arr1[i]
        elif mask%3 == 1:
            total += arr2[i]
        else: total = total + arr1[i] + arr2[i]
        mask //= 3
    return total

if __name__ == '__main__':
    count = 0
    sumy = []
    for mask in range(3**n):
        if is_prime(generate_totals(mask)):
            sumy.append(generate_totals(mask))
            count += 1
    print(count)
    print(set(sumy))