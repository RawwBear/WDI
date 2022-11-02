'''
Find longest subsequence in given array that reverse version of the subsequence also exist in the array.
'''
from random import randrange

def reverse_subseq_onedigit():
    '''
    Function works for numbers between 0 and 9 inclusive, because for 3digit numbers it reverse subseq change order of
    the digits in the nubmer e.g. subseq = [200, 315] reverse_ss should be [315, 200] not [513, 002].

    I assume that array can't be empty, n > 0
    '''
    array = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
    seq = ''.join(map(str, array))
    print(seq)
    long_subseq = ''
    counter, max_counter = 1, 1 #I assume that the reverse subseq to one-element subseq is itself
    if len(seq) == 1: return 1
    else:
        i, j = 0, 1#I assume that sequence has at least 2 elements
        while i < len(seq)-2:
            subseq = seq[i:j + 1]
            # print(subseq)
            # print(subseq[::-1])
            if subseq[::-1] in seq[j+1:]:
                counter += 1
            else:
                i += 1
            j += 1
            if counter > max_counter:
                max_counter = counter
                long_subseq = subseq

    return max_counter, long_subseq

def reverse_ss(n):
    '''
    Function assumes that number present in subsequence can't be part of reverse subseq.
    '''
    array = [randrange(100, 1000) for _ in range(n)]
    # array = [234, 890, 200, 315, 876, 123, 101, 256, 315, 200, 256, 101, 123]
    seq = ','.join(map(str, array))
    long_subseq = ''
    # print(seq)
    counter, max_counter = 1, 1  # I assume that the reverse subseq to one-element subseq is itself
    if len(array) == 1:
        return 1
    else:
        i, j = 0, 1  # I assume that sequence has at least 2 elements
        while i < len(array) - 2:
            ss_arr = array[i:j + 1]
            rev_ss_arr = ss_arr[::-1]
            subseq = ''.join(map(str, ss_arr))
            seq_after_ss = ''.join(map(str,array[j + 1:]))
            rev_ss =  ''.join(map(str,rev_ss_arr))
            # print(seq_after_ss)
            # print(rev_ss)
            if rev_ss in seq_after_ss:#check if reversed subseq is in the next part of the sequence after ss
                #after ss and rev_ss in the seq length of the checking seq is changed to the longest ss, only longest can replace it
                counter += 1
            else:
                i += 1
            j += 1
            if counter > max_counter:
                max_counter = counter
                long_subseq = subseq

    return max_counter


if __name__ == '__main__':
    print(reverse_subseq_onedigit())
    print(reverse_ss(10))
