from random import randrange

def is_composed(num):
    if num < 4:
        return False
    if num == 4: return True
    i = 5
    while i < int(num**(0.5))+1:
        if num % i == 0: return True
        i += 2
        if num % i == 0: return True
        i += 4
    return False


def check_around(i, j, n, array):#we take cords of element with check around (i,j),
    combination = [(1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (0, 1), (0, -1), (-1, 1)]#moves to neighbours
    not_comp = 0
    for x, y in combination:
        if i+x > n-1 or i+x < 0 or j+y > n-1 or j+y< 0:#we are out of the array
            continue
        else:
            if not is_composed(array[x+i][y+j]): not_comp += 1#every cell can have maximum of 8 neighbours in 2d array,
            # so if is there 2 or more not composed numbers we can't have 6 neigbours
    if not_comp > 2: return False
    return True



def six_neighbours_3d(n):
    array = [[[randrange(1, 31) for _ in range(n)]for _ in range(n)]for _ in range(n)]
    print(array)
    #we need to take out 6 two-dimensial arrays
    level_neighbours = 0
    for i in range(1, n):  #check how many elements with >= 6 neighbours in the first level
        for j in range(n):
            level_neighbours += check_around(i, j, n, array[0])
    for z in range(1,6):
        arr_2d = array[z]
        count = 0
        for i in range(1, n):#start from second row
            for j in range(n):
                count += check_around(i, j, n, arr_2d)
        if level_neighbours != count:
            return False
    return True

if __name__ == '__main__':
    print(six_neighbours_3d(5))