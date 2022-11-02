from random import randrange

def odd_digits(n):
    array = [randrange(1, 1001) for _ in range(n)]
    print(array)
    for elem in array:
        is_odd = False
        for digit in str(elem):
            if int(digit)%2 != 0:
                is_odd = True
                break
        if is_odd == False:#return False if in the list is at least one number with only even digits
            return False
    return True
if __name__ == '__main__':
    print(odd_digits(10))