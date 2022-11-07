from random import randrange
def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i < int(num**(0.5))+1:
        if num % i == 0: return False
        i += 2
        if num % i == 0: return False
        i += 4
    return True

def zero_out(n):
    array = [[randrange(1,37) for _ in range(n)]for _ in range(n)]
    for i in range(n):
        print(array[i])
    linear_arr = []
    for i in range(n):#create 1-dimensial array from 2-dimensial array
        for j in range(n):
            linear_arr.append(array[i][j])
    for i in range(len(linear_arr)-1):
        flag = False
        for j in range(i+1, len(linear_arr)):
            suma = linear_arr[i] + linear_arr[j]
            if is_prime(suma):
                flag = True
                break
        if flag == False: linear_arr[i] = 0
    return linear_arr
if __name__ == '__main__':
    print(zero_out(4))
