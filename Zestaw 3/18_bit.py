def ss_odd_nums():
    array = [4, 9, 4, 5, 2, 9, 7, 15, 7, 9, 1]
    n = len(array)
    longest = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = True
            len_ss = j - i + 1
            for k in range(len_ss//2 + 1):
                if array[i + k] != array[j - k] or array[i + k]%2 == 0 or array[j - k]%2 == 0:
                    flag = False
                    break
            if flag:
                longest = max(longest, len_ss)
    return longest


def ss_odd_faster():
    pass



if __name__ == '__main__':
    print(ss_odd_nums())