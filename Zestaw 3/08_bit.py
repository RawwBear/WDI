from random import randrange

def from_zero_to_end(t:[]):
    n = len(t)
    array = [False for _ in range(n)]
    array[0] = True
    #array filled with False statements, when we jump into certain index number we will change value to the True
    for k in range(n):#for some k nothing change
        if array[k] == True:#works only when we jump into this place in the array
            curr_num = t[k]
            i = 2
            while curr_num != 1:#change all jumps into T[k+i] where i - is prime factor for curr_number and k is index where we start our jump
                while curr_num % i == 0:
                    if k + i < n:#if starting index + prime factor index < len(array) then change value in array[k+i] to True
                        array[k + i] = True
                    curr_num //= i
                i += 1
    return array[n-1]
if __name__ == '__main__':
    print(from_zero_to_end([6, 1, 5, 2, 4, 3, 9, 9, 1, 2, 4]))
    print(from_zero_to_end([randrange(1, 11) for _ in range(10)]))