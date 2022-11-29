from random import randrange
chess_board = [[randrange(1, 26)for _ in range(8)]for _ in range(8)]
for i in range(8):
    print(chess_board[i])

def zad3(chess_board, col):

    def count_total(chess_board, col, row=0):
        #end conditions
        if row == 7: return chess_board[row][col]
        if col > 0:
            left = count_total(chess_board,col-1, row+1)
        else:
            left = float('inf')
        if col < 7:
            right = count_total(chess_board, col+1, row+1)
        else:
            right = float('inf')
        mid = count_total(chess_board, col, row+1)

        return  min(left, mid, right) + chess_board[row][col]
    return count_total(chess_board,col)

print(zad3(chess_board,5))