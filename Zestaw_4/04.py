from random import randrange
def sum_elem_row(arr):
    count = 0
    for elem in arr:
        count += elem
    return count

def sum_elem_col(id_col, arr):
    count = 0
    for row in range(len(arr)):
        count += arr[row][id_col]
    return count

def bigesst_quotient(n):
    array = [[randrange(1, 31) for _ in range(n)] for _ in range(n)]#created arrey filled with random numbers
    res = (0, 0)
    for i in range(n):#print array row after row
        print(array[i])
    quotient, max_quo = 0, 0
    for i in range(n):
        sum_row = sum_elem_row(array[i])
        for j in range(n):
            sum_col = sum_elem_col(j, array)
            quotient = sum_row/sum_col
            if quotient > max_quo:
                max_quo = quotient
                res = (i, j)
    return quotient, res


if __name__ == '__main__':
    print(bigesst_quotient(5))