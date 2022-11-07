from random import randrange

def same_digits(a, b):
    digits_a = []
    while a != 0:
        digit = a%10
        if digit not in digits_a:
            digits_a.append(digit)
        a //= 10
    while b != 0:
        if b%10 not in digits_a:
            return False
        b //= 10
    return True

array = [[211, 211111, 2122, 221, 12], [21, 12, 221, 5, 211],[2, 122, 17, 14, 3], [7, 6, 8, 13, 544], [9, 10, 11, 45, 54]]
def check_neighhours(x,y, curr_elem, n):
    if x > 1:
        if same_digits(curr_elem,array[x-1][y]) == False: return False
    if x < n-1:
        if same_digits(curr_elem, array[x+1][y]) == False: return False
    if y < n-1:
        if same_digits(curr_elem, array[x][y+1]) == False: return False
    if y > 1:
        if same_digits(curr_elem, array[x][y-1]) == False: return False
    return True

def friendly_nums():
    n = len(array)
    for i in range(n):
        print(array[i])
    count = 0
    for i in range(n):
        for j in range(n):
            curr_elem = array[i][j]
            if check_neighhours(i, j, curr_elem, n):
                count+=1
    return count

if __name__ == '__main__':
    print(friendly_nums())

