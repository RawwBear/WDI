def seq_ascending(seq):
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]: return False
    return True

def index_sum():
    array = [6, 7, 1, 3, 5, 11]
    curr_len, max_len = 1, 1
    for i in range(len(array)-1):
        sum_val, sum_idx = 0, 0
        sum_idx += i
        sum_val += array[i]
        for j in range(i+1, len(array)):
            if seq_ascending(array[i:j+1]) == False:
                break
            else:
                sum_idx += j
                sum_val += array[j]
                curr_len += 1
                if sum_idx == sum_val:
                    if curr_len > max_len:
                        max_len = curr_len
        curr_len = 1
    if max_len != 1: return max_len
    else: return 0

if __name__ == '__main__':
    print(index_sum())