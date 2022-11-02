def sieve(n):
    A = [1]*n
    A[0] = 0
    A[1] = 0
    for i, elem in enumerate(A):
        if elem == 0:
            continue
        if elem == 1:
            a = i
        a += i
        while a < n:#each multiple of current prime number is assigned the value one
            A[a] = 0
            a += i
    return A

for i,v in enumerate(sieve(int(input("Enter n value: ")))):
    if v == 1:
        print(i)
