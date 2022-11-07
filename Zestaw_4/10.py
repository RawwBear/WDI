
from random import randrange
# array = [[randrange(0,6)for _ in range(n)]for _ in range(n)]
array = [[0, 3, 0, 2, 0],
        [0, 1, 4, 3, 0],
        [3, 1, 5, 0, 5],
        [0, 0, 5, 1, 3],
        [0, 1, 2, 3, ]]

def check_for_zero(array):
    n = len(array)
    for i in range(n):
        print(array[i])

    columns = [False for _ in range(n)]#arrays filled with False statements, if 0 in certain index of columns
    # then columns[idx] = True what means that in every column zero appears

    for i in range(n):
        flag = False
        for j in range(n):
            if array[i][j] == 0:
                flag = True
                columns[j] = True
                if False not in columns and flag == True: break
        if flag == False: return False
    if False in columns: return False
    return True

if __name__ == '__main__':
    print(check_for_zero(array))
