from random import randrange
import math
def are_compatible(a):
    count = 0
    while a != 0:
        if a%2 == 1: count += 1
        a = a//2
    return count

a_small = [[2, 1, 2], [6, 7, 7], [6, 7, 3]]
a_big = [[6, 5, 9, 1, 8],
         [1, 2, 4, 2, 8],
         [1, 6, 2, 7, 7],
         [5, 1, 7, 3, 4],
         [8, 2, 2, 2, 2]]

for i in range(3):
    print(a_small[i])
for i in range(5):
    print(a_big[i])
def check_for_overlap(i,j,m,new_small, new_big):
    count = 0
    for x in range(m):
        col = j
        for y in range(m):
            if new_big[i][col] == new_small[x][y]:
                count += 1
                col += 1
        i += 1
    return count
def find_location(a_small, a_big):
    n = len(a_big)
    m = len(a_small)
    procent = math.ceil(m*m/3)
    new_small = [[are_compatible(a_small[i][j])for i in range(m)]for j in range(m)]
    new_big = [[are_compatible(a_big[i][j]) for i in range(n)] for j in range(n)]
    # n>m
    for i in range(n-m+1):
        for j in range(n-m+1):
            count = check_for_overlap(i,j,m, new_small, new_big)
            if count >= procent:
                return True
    return False

if __name__ == '__main__':
    print(find_location(a_small, a_big))