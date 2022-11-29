from random import randrange
def ss_sum(arr:[]):
    i, j = 0, 1
    max_sum = 0
    while j < n:
        count += linear_row[i]
        while linear_row[j] > 0:
            count += linear_row[j]
            j += 1
        if count > max_sum:
            max_sum = count
        i = j + 1
        j = i + 1
    return max_sum
def ss_with_biggest_sum(n):#array linarization isn't good option for this problem
    array = [[randrange(-20, 31)for _ in range(n)]for _ in range(n)]
    for i in range(n):
        print(array[i])
    #create two 1D arrays for elements of the 2D array by rows and by columns
    linear_row, linear_col = [array[i][j] for i in range(n) for j in range(n)], [array[j][i] for i in range(n) for j in range(n)]
    res_row, res_col = ss_sum(linear_row), ss_sum(linear_col)
    if res_col > res_row:
        return res_col
    return res_row

if __name__ == '__main__':
    print(ss_with_biggest_sum(5))