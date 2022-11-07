from random import randrange
def ss_with_biggest_sum(n):
    array = [[randrange(-20, 31)for _ in range(n)]for _ in range(n)]
    for i in range(n):
        print(array[i])
    #create two 1D arrays for elements of the 2D array by rows and by columns
    linear_row, linear_col = [array[i][j] for i in range(n) for j in range(n)], [array[j][i]for i in range(n) for j in range(n)]
    max_sum = 0
    l, r = linear_row[0], linear_row[1]
    while l < n-1:
        if array[l] + array[r] > max_sum:
            max_sum = array[l] + array[r]
if __name__ == '__main__':
    print(ss_with_biggest_sum(5))