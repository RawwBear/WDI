from random import randrange

def long_arithmetic_subseq():
    # array = [randrange(1, 31) for _ in range(n)]
    # print(array)
    array = [1, 3, 5, 7, 3, 17]
    r = array[0] - array[1]
    counter, max_counter = 2, 2
    i = 1
    while i < len(array) - 2:
        while array[i] - array[i+1] == r and i < len(array) - 2:
            counter += 1
            i += 1
        r = array[i] - array[i+1]
        if counter > max_counter:
            max_counter = counter
        counter = 1
        i += 1
    return max_counter

if __name__ == '__main__':
    print(long_arithmetic_subseq())