def is_valid(elem, curr_product):
    #we don't increase the value of curr_product we only chack if next value in the array (elem) can be part of the
    # sequence it means there is no same prime factors for elem as for curr_product

    if curr_product % elem == 0: return False
    divisor = 2
    already_divided = False
    while elem != 1:
        if elem % divisor == 0:
            if curr_product % divisor == 0 or already_divided: #divisor already is prime factor of curr_product or elem have two same prime factors
                return False
            already_divided = True
            elem //= divisor
        else:
            divisor += 1
            already_divided = False
    return True


def ss_prime_fac(t:[]):
    #function need to return value of the longest consistent subsequence for which in the product of its elements the
    #prime factors are not repeated
    i, j = 0, 0 #create pointers with which we will pass through elements of the given array, j - at the end, i - at the start of searched ss
    curr_len, max_len = 1, 1
    curr_product = t[0]
    while j < len(t) - 1:
        if is_valid(t[j+1], curr_product):
            j += 1
            curr_product *= t[j]
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        else:
            if curr_product == 1:
                i += 1
                j += 1
            else:
                curr_product //= t[i]
                curr_len -= 1
                i += 1
    return max_len

if __name__ == '__main__':
    print(ss_prime_fac([2, 2, 33, 35, 7, 4, 6, 7, 6, 11, 13, 5]))
    print(is_valid(9, 45))