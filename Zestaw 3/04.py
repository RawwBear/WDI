''''
Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
'''
def determine_e(n):
    e = 1
    factorial = 1
    i = 1
    digits = []
    while i != n:
        e += 1 / factorial
        print(e)
        i += 1
        factorial *= i

if __name__ == "__main__":
    print(determine_e(10))