from random import randrange
n = int(input("Enter value of the n: "))
array = [[randrange(-20, 31)for _ in range(n)]for _ in range(n)]
for i in range(n):
    print(array[i])

def count_sum(i,j,n):
    len_horizon, len_vertical = 1, 1
    sum_horizon, sum_vertical = array[i][j], array[i][j]
    x, y = i+1, j+1
    #add up horizontally
    while x < n and len_horizon < 10:
        sum_horizon += array[x][j]
        len_horizon += 1
        x +=1
    while y < n and len_vertical < 10:
        sum_vertical += array[i][y]
        len_vertical += 1
        y += 1
    if sum_horizon > sum_vertical:
        return sum_horizon
    return sum_vertical

def sum_ss():
    maxi = 0
    for i in range(n):
        for j in range(n):
            count = count_sum(i,j,n)
            if count > maxi:
                maxi = count
    return maxi

if __name__ == '__main__':
    print(sum_ss())