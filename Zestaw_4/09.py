from random import randrange

# arr = [[randrange(1, 16)for _ in range(6)] for _ in range(6)]
arr = [[11, 13, 8, 9, 5, 6],
[7, 12, 7, 14, 7, 6],
[3, 12, 9, 6, 6, 14],
[7, 4, 11, 12, 10, 14],
[12, 12, 8, 1, 9, 15],
[4, 14, 15, 1, 14, 15]]


for i in range(len(arr)):
    print(arr[i])

def square(arr, k):
    #I assume that arr is not smaller than 3x3
    n = 3
    m = len(arr)
    while n <= m:
        for i in range(m-n+1):
            for j in range(m-n+1):
                print(arr[i][j],arr[i][j+n-1],arr[i+n-1][j],arr[i+n-1][j+n-1], sep= ' ', end= '\n')
                if arr[i][j]*arr[i][j+n-1]*arr[i+n-1][j]*arr[i+n-1][j+n-1] == k:
                    return f'Square found, coordinates of the mid are: {(i+n//2,j+n//2)}'
        n += 2
    return "Square not found"
if __name__ == '__main__':
    print(square(arr, 2520))