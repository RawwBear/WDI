from random import randrange

def leng_of_longest_ascending_subseq(n):
    array = [randrange(1, 51) for _ in range(n)]
    print(array)
    counter, max_count = 1, 1
    i = 0
    subseq = []
    while i < len(array)-2:
        start = i
        while array[i] < array[i+1] and i < len(array)-2:
            counter += 1
            i += 1
        if counter > max_count:
            max_count = counter
            subseq=array[start:i+1]
        counter = 1
        i += 1
    return max_count, subseq

if __name__ == '__main__':
    print(leng_of_longest_ascending_subseq(10))