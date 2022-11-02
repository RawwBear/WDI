
def fill_arr(n):
    array = [[0 for _ in range(n)] for _ in range(n)]#array filled with zeros
    i = 0
    while i < n:
        for j in range(n):
            array[i][j] = n*i + j
        i += 1
    for i in range(n):
        print(array[i])

if __name__ == '__main__':
    print(fill_arr(5))