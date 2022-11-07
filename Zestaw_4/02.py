from random import randrange

def odd_digit_num(num):
    while num != 0:
        digit = num%10
        if digit % 2 == 0: return False
        num //= 10
    return True
def is_array(n):
    array = [[randrange(1, 31) for _ in range(n)] for _ in range(n)]#created arrey filled with random numbers

    for i in range(n):#print array row after row
        print(array[i])

    for i in range(n):
        flag = False
        for j in range(n):
            num = array[i][j]
            if odd_digit_num(num):
                flag = True
                break
        if flag == False: return False
    return True



if __name__ == '__main__':
    print(is_array(5))