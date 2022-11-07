from random import randrange
#I assume neighbors of the element can be vertical, horizontal and diagonal
def sum_neighbours(x, y, n, array):
    suma = 0
    coordninates = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i, j in coordninates:
        if x + i> n - 1 or x - i < 0 or y + j > n - 1 or y - j < 0:
            continue
        else:
            suma += array[x+i][y+j]
    return suma
def biggest_sum_neighbours(n):
    array = [[randrange(1, 37) for _ in range(n)] for _ in range(n)]
    max_sum, elem = 0, (0,0)
    for i in range(n):
        print(array[i])
    for i in range(n):
        for j in range(n):
            suma = sum_neighbours(i, j, n, array)
            if suma > max_sum:
                max_sum = suma
                elem = (i, j)
    return max_sum, elem

if __name__ == '__main__':
    print(biggest_sum_neighbours(5))



