from random import randrange
def geometric_subseq(n):
    array = [randrange(1, 51) for _ in range(n)]
    print(array)
    # array = [3, 1, 4, 8, 2, 9, 27, 81, 15, 5, 1]
    counter, max_counter = 2, 2
    q = array[1]/array[0]
    for i in range(1, len(array)-2):
        if array[i+1]/array[i] == q:
            counter += 1
        else:
            q = array[i+1]/array[i]
            counter = 2
        if counter > max_counter:
            max_counter = counter
    return max_counter

if __name__ == '__main__':
    print(geometric_subseq(10))