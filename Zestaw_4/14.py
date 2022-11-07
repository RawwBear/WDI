from random import randrange
def are_compatible(a):
    count = 0
    while a != 0:
        if a%2 == 1: count += 1
        a = a//2
    return count

a_small = [[2, 4, 2], [6, 2, 7], [1, 7, 3]]
a_big = [[6, 5, 9, 1, 8],
         [1, 2, 4, 2, 8],
         [1, 6, 2, 7, 7],
         [5, 1, 7, 3, 4],
         [8, 2, 2, 2, 2]]

for i in range(3):
    print(a_small[i], end='\n')
for i in range(5):
    print(a_big[i], end='\n')

def is_comp_row(col_s,row_s, col_b, row_b):
    m = len(a_small)
    while row_b < m:
        row_s += 1
        row_b += 1
        if a_big[col_b][row_b] != a_small[col_s][row_s]:
            return False
    return True

# print(is_comp_row(1, 1, 2, 2))

def arrays():
    n, m = len(a_big), len(a_small)
    new_tab = []
    small_row = a_small[0]
    left_corner = (0, 0)
    for col_s in range(m):
        for row_s in range(m):
            elem = a_small[col_s][row_s]
            for col_b in range(n):
                for row_b in range(n):
                    if a_big[col_b][row_b] == elem:
                        # left_corner = (col_b,row_b)
                        if a_big[col_b][row_b:row_b + 3] == a_small[col_s]:
                            new_tab.append(a_small[col_s])
                            break

    new_tab.pop(0)
    return new_tab







def cut():
    new_tab = []
    n, m = len(a_big), len(a_small)
    for col_b in range(n):
        col_s = 0
        for row_b in range(n):
            if a_big[col_b][row_b] == a_small[col_s][row_s]:
                if a_big[col_b][row_b:row_b + 3] == a_small[col_s] and col_s < len(a_small):
                    new_tab.append(a_small[col_s])
                    col_s += 1
    return new_tab


# print(cut())


print(arrays())
