def fill_after_spiral(n):
    array = [[0 for _ in range(n)] for _ in range(n)]  # array filled with zeros
    v = 1
    first_row, last_row = 0, n - 1
    first_col, last_col = 0, n-1
    while v <= n*n:
        for j in range(first_col, last_col+1):#complete first row
            array[first_row][j] = v
            v += 1
        first_row += 1
        for i in range(first_row, last_row+1):#complete last column
            array[i][last_col] = v
            v += 1
        last_col -= 1
        for j in range(last_col, first_col-1, -1):#complete last row
            array[last_row][j] = v
            v += 1
        last_row -= 1
        for i in range(last_row, first_row-1, -1):#complete first column
            array[i][first_col] = v
            v += 1
        first_col += 1

    for i in range(n):#print matrix
        print(array[i])

if __name__ == '__main__':
    print(fill_after_spiral(5))