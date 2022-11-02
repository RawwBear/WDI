from random import randrange

def longest_subseq(n):
    array = [randrange(1, 100, 2) for _ in range(n)]
    # array = [3, 5, 7, 9, 11, 9, 7, 5, 2, 13, 17, 21, 33, 66]
    count_positive, count_negative = 0, 0
    max_positive, max_negative = 0,0
    print(array)
    r = array[1] - array[0]
    if r > 0: count_positive += 2
    else: count_negative += 2
    for i in range(1, len(array)-2):
        if array[i+1]-array[i] == r:
            if r > 0:count_positive += 1
            else: count_negative += 1
        else:
            r = array[i+1]-array[i]
            if r > 0: count_positive = 2
            else: count_negative = 2
        if count_positive > max_positive:
            max_positive = count_positive
        if count_negative > max_negative:
            max_negative = count_negative
    return max_positive - max_negative

if __name__ == '__main__':
    print(longest_subseq(10))