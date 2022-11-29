from random import randrange
from math import inf
def find_row(array, leader_board):
    curr = 0
    for i in range(1, len(array)):
        if array[curr][leader_board[curr]] > array[i][leader_board[i]]:
            curr = i
    return curr#return row with smallest value

def retype(n):
    array = [sorted([randrange(1, 26) for _ in range(n)]) for _ in range(n)]
    for i in range(n):
        print(array[i])
    row = 0
    arr2_idx = 0
    prev_value = -1
    arr2 = [0 for _ in range(n*n)]
    leader_board = [0 for _ in range(n)]#indexes are equivalent to row number of the array, values of leader board
    #correspond to column number with smallest value of the array
    for i in range(n*n):
        row = find_row(array, leader_board)#number of column in array with smallest value
        if prev_value != array[row][leader_board[row]]:
            prev_value = arr2[arr2_idx] = array[row][leader_board[row]]
            arr2_idx += 1
        if leader_board[row] == n-1: array[row][leader_board[row]] = inf
        else:leader_board[row] += 1
    return arr2
if __name__ == '__main__':
    print(retype(5))