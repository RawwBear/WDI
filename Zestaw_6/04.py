board = [[0 for _ in range(6)]for _ in range(6)]

def contains(n, col, row):
    if 0 <= col < n and 0 <= row < n:
        return True
    return False

def knight_walk(board, col, row, cnt=1):
    n = len(board)
    board[row][col] = cnt
    if cnt == n*n:#we filled the whole array with nubmers from 1 do n*n
        return True

    jumps = [(-1,2), (-1,-2), (1, 2), (1, -2), (-2,1), (-2, -1), (2, 1), (2, -1)]
    for jump in jumps:
        next_row = row + jump[0]
        next_col = col + jump[1]
        if contains(n, next_col, next_row) and board[next_row][next_col] == 0:#we can jump into this filed and assing cnt value to this filed
            if knight_walk(board, next_col, next_row, cnt+1):
                return True
    board[row][col] = 0#zmieniamy wartosc pola na zero tak jakby skoczek nigdy nie był na tym polu, bo nie było z niego żadnego możliwego skoku
    return False

print(knight_walk(board,4,1))
for row in board:
    print(row)
