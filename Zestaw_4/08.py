from random import randrange

# array = [[8,9,10,1,2], [3,4,3,9,2], [6,7,2,1,8], [11,12,13,1,5], [2,14,15,7,6]]
# n = len(array)

def count_seq_geomet(row, col, array):
    n = len(array)
    count = 2
    q = array[row][col]/array[row+1][col+1]
    while row < n-2 and col < n-2:
        row += 1
        col += 1
        if array[row][col]/array[row+1][col+1] == q:
            count += 1
        else: break
    return count


def geomet_seq_diagonally(n):
    array = [[randrange(1,37) for _ in range(n)]for _ in range(n)]

    for i in range(n):
        print(array[i])

    max_count = 2
    for i in range(n-2):
        for j in range(n-2):
            curr_elem = array[i][j]
            count = count_seq_geomet(i, j, array)
            if count > max_count:
                max_count = count
    if max_count > 2: return max_count
    else: return "Sequence not found"

if __name__ == '__main__':
    print(geomet_seq_diagonally(5))

