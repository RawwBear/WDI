from random import randrange

def even_digit_num(num):
    while num != 0:
        digit = num%10
        if digit%2 == 0: return True
        num //= 10
    return False

def is_array(n):
    array = [[randrange(1, 31) for _ in range(n)] for _ in range(n)]#created arrey filled with random numbers

    for i in range(n):#print array row after row
        print(array[i])

    for i in range(n):
        for j in range(n):
            num = array[i][j]
            if even_digit_num(num) == False: return False
    return True



if __name__ == '__main__':
    print(is_array(5))

