from random import randrange
n= int(input("Enter the n: "))
array = [[randrange(1, 13)for _ in range(n)]for _ in range(n)]
for i in range(n):
    print(array[i])

def calc_sum(array, sum_rows, sum_colums, i, j, x, y):
    if i == x: #rooks stay in the same row
        return sum_colums[j] + sum_colums[y] + sum_rows[i] - array[i][j] - array[x][y]
    if j == y:#rooks stay in the same column
        return sum_colums[j] + sum_rows[x] + sum_rows[i] - array[i][j] - array[x][y]
    #rooks stay in different columns and different rows
    return sum_colums[j] + sum_rows[i] + sum_rows[x] + sum_colums[y] - 2*array[i][j] - 2*array[x][y] - array[i][y] - array[x][j]

def set_rooks():
    sum_rows, sum_columns = [0 for _ in range(n)], [0 for _ in range(n)]#store sums in every column and row,
    # e.g. sum_rows = sum of values in the row with index equal to 0
    for i in range(n):
        count_row = 0
        count_col = 0
        for j in range(n):
            count_row += array[i][j]
            count_col += array[j][i]
        sum_rows[i] = count_row
        sum_columns[i] = count_col
    max_sum = 0
    rook1, rook2 = (0,0), (0,0)
    for i in range(n):
        for j in range(n):
            for x in range(i, n):
                for y in range(j, n):
                    if x == i and y == j:
                        continue
                    tmp_sum = calc_sum(array, sum_rows, sum_columns, i, j , x, y)
                    if tmp_sum > max_sum:
                        max_sum = tmp_sum
                        rook1, rook2 = (i, j), (x, y)
    return rook1, rook2




if __name__ == '__main__':
    print(set_rooks())
