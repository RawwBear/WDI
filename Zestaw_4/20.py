import copy
from random import randrange
n= int(input("Enter the n: "))
T = [[randrange(1, 13)for _ in range(n)]for _ in range(n)]

for i in range(n):
    print(T[i])
#1attempt: I don't consider move of two towers at once, as to find biggest sum of the fields but have in mind that
#rooks can check the same field and then we sum same box twice. I made this solution as find two biggest sums separetly.
def tower_move(row, col, T, n):
    count = 0
    array = T
    plus = 1;
    minus = -1
    while plus + row < n or minus + row >= 0 or plus + col < n or minus + col >= 0:
        if plus + row < n:
            count += array[plus + row][col]
        if plus + col < n:
            count += array[row][plus + col]
        plus += 1
        if minus + row >= 0:
            count += array[minus + row][col]
        if minus + col >= 0:
            count += array[row][minus + col]
        minus -= 1
    return count

def set_towers():
    max1, max2 = 0, 0
    cord1, cord2 = (0,0), (0,0)
    for row in range(n):
        for col in range(n):
            count = tower_move(row, col, T, n)
            if count > max1:
                max1, max2 = count, max1
                cord1, cord2 = (row,col), cord1
            elif count > max2:
                max2 = count
                cord2 = (row, col)
    return cord1, cord2

#2. I need to move two rooks at once and searching their common sum.
def common_sum(row, col, array, n):
    count = 0
    plus = 1;
    minus = -1
    while plus + row < n or minus + row >= 0 or plus + col < n or minus + col >= 0:
        if plus + row < n:
            count += array[plus + row][col]
            array[plus + row][col] = 0
        if plus + col < n:
            count += array[row][plus + col]
            array[row][plus + col] = 0
        plus += 1
        if minus + row >= 0:
            count += array[minus + row][col]
            array[minus + row][col] = 0
        if minus + col >= 0:
            count += array[row][minus + col]
            array[row][minus + col] = 0
        minus -= 1
    for i in range(n):
        print(array[i])
    print()
    max_sum, cord2 = 0, (0,0)
    for x in range(row, n):
        for y in range(col, n):
            suma = count + tower_move(x, y, array, n)
            if suma > max_sum:
                max_sum = suma
                cord2 = (x,y)
    return (max_sum, cord2, (row, col))

def set_rooks():
    max_sum = 0
    result = ()
    for row in range(n):
        for col in range(n):
            array = [i.copy() for i in T]#same as array = copy.deepcopy(T)
            # array = copy.deepcopy(T)
            for i in range(n):
                print(array[i])
            print()
            cnt = common_sum(row, col, array, n)
            if cnt[0] > max_sum:
                max_sum = cnt[0]
                result = cnt
    return result


if __name__ == '__main__':
    print(set_towers())
    print(set_rooks())