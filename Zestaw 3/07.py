from random import randrange

def only_odd_digits(n):
    array = [randrange(1, 1001) for _ in range(n)]
    print(array)
    for elem in array:
        is_even = False
        for digit in str(elem):
            if int(digit)%2 == 0:
                is_even = True
                break
        if is_even == False:#return False if in the list is at least one number with only even digits
            return True
    return False
if __name__ == '__main__':
    print(only_odd_digits(20))