def is_valid(n, product):#n is next element in the sequence, product is curr_product of the ss
    if product % n == 0:
        return False
    divisor = 2
    already_divided = False
    while n > 1:
        if n % divisor == 0:
            if product % divisor == 0 or already_divided:
                return False
            already_divided = True
            n //= divisor
        else:
            divisor += 1
            already_divided = False
    return True


def ss_prime_factors(t):
    i, j = 0, 0
    curr_len, max_len = 1, 1
    curr_product = t[0]
    while j != len(t) - 1:
        if is_valid(t[j + 1], curr_product):
            curr_product *= t[j + 1]
            j += 1
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        else:
            if curr_product == 1:
                i += 1
                j += 1
            else:
                curr_product //= t[i]
                i += 1
                curr_len -= 1
    return max_len


if __name__ == '__main__':
    print(ss_prime_factors([2, 2, 33, 35, 7, 4, 6, 7, 6, 11, 13, 5]))
    print(is_valid(23, 2))