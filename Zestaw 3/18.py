from random import randrange
#TO IMPROVE

# n = int(input("Enter size of the array: "))
# array = [randrange(1, 21, 2) for _ in range(n)]
# print(array)
def is_palindrome(array):
    return array == array[::-1]

def subseq_slice():
    # array = [3, 9, 15, 5, 19, 15, 7, 15, 5, 7]
    array = [8, 9, 7, 9, 0, 5, 7, 3, 3, 7, 5]
    seq = []#seq is the longest subsequence composed only of odd nubmers
    res = []
    counter, max_counter = 0, 0
    j, i = 0, 0
    for i in range(len(array)):
        if array[i]%2 != 0:
            seq = array[j:i+1]
            counter += 1
        if array[i]%2 == 0 or i == len(array)-1:
            if len(seq) > 1 and counter > max_counter:
                for x in range(len(seq)-1):
                    for y in range(x + 1, len(seq)):
                        if is_palindrome(seq[x:y+1]):
                            if counter > max_counter:
                                max_counter = counter
                                res = seq[x:y+1]
            seq = []
            counter = 0
            j = i + 1
    return max_counter, res

def subseq_pop():#Here we have a bug
    # works if we have palindromes separated by even numbers ... doesn't work if palindrom is among odd numbers
    array = [8, 9, 7, 9, 0, 5, 7, 3, 3, 7, 8]
    count, max_count = 0, 0
    seq = []
    while len(array) > 0:
        if array[0]%2 == 0:
            array.pop(0)
            seq = []
            count = 0
        else:
            seq.append(array.pop(0))
            count += 1
        if len(seq) > 1 and is_palindrome(seq) and count > max_count:
            max_count = count
            print(seq)
    return max_count




if __name__ == '__main__':
    # print(is_palindrome([13,4,13]))
    print(subseq_slice())
    print(subseq_pop())