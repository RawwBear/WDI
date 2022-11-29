from random import randrange
n, product = int(input("Enter the n: ")), int(input("Enter the product: "))
array = [[randrange(1, 13)for _ in range(n)]for _ in range(n)]
for i in range(n):
    print(array[i])
def chess_jumper_move(row, col, array, n, product):
    #for every element when jumper starts his move we can have max one pair with givern product, because
    #for every element which is pair with checked one there will be repetions because so we only check is there any pair
    #for checked element.
    cords = [(2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (-1, 2), (1, -2), (-1, -2)]
    for x, y in cords:
        if row + x < n and row + x >= 0:
            if col + y < n and col + y >=0:
            #we are now sure that jumper won't fall off the board
                if array[x+row][y+col]*array[row][col] == product:
                    return True
    return False

def pairs():
    count = 0
    for row in range(n):
        for col in range(n):
            if chess_jumper_move(row, col, array, n, product):
                count += 1
    return count

if __name__ == '__main__':
    print(pairs())

