#Wrtie function which sum elements of the sequence and return sum using recursion
from random import randrange, getrandbits
array = [randrange(0,11)for _ in range(8)]
print(array)
def suma(array,i=0):
    n = len(array)
    if i > n - 1:
        return 0
    return array[i] + suma(array,i+1)

#Write function which will count n eleement of fibonacci sequence using recursion
def count_fibo(n):
    if n == 1 or n == 2: return 1
    return count_fibo(n-1) + count_fibo(n-2)


#Check whether the (bool) array has at least one True value
bool_array = [bool(getrandbits(1))for _ in range(5)]
print(bool_array)
def check_True(bool_array,i=0):
    n = len(bool_array)
    if i > n - 1: return False
    #if i == n - 1: return bool_array[i] #also works
    return bool_array[i] or check_True(bool_array, i + 1)

#Check whether the bool array has two True values after each other
def check(bool_array, i=0):
    n = len(bool_array)
    if i == n - 2:
        return bool_array[i] and bool_array[i+1]
    # if i > n - 2: return False #also works as end condition
    return (bool_array[i] and bool_array[i+1]) or check(bool_array, i+1)


if __name__ == '__main__':
    print(suma(array))
    print(count_fibo(12))
    print(check_True(bool_array))
    print(check(bool_array))