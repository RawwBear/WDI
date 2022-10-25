'''
Find smallest base for two numbers where both of them don't have any common digits. REMARK: Numbers in systems 11 to 16
contains also letters, but we gonna omitt them because goal for this program is to find smallest base where both numbers
have different numbers or print that base doesn't exist, it makes tasks more easier.
'''
def change_bases(num, base):#works for systems from 2 to 9
    result = ''
    if base < 10:
        while num != 0:
            result += str(num%base)
            num //= base
    else:#we will omitt letters, but we lengths of two numbers in systems with base > 10 can be different
        while num != 0:
            if num%base > 9:
                num //= base
            else:
                result += str(num % base)
                num //= base
    return result[::-1]


def is_diff_digits(a: str):#checks that the digits in a number are not repeated
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return False
    return True

def diff_digit_num(a, b):#checks that the digits in a numbers are all different
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return False
    return True


def smallest_base(a, b):
    for i in range(2, 17):
        if i == 10:
            res_a = str(a)
            res_b = str(b)
        else:
            res_a = change_bases(a, i)
            res_b = change_bases(b, i)
        if diff_digit_num(res_a, res_b) == True:
            return i
    return False


'''
Solution by Karatkevich.
1. Create list 16*16 filled with zeros. 
2. Iterate over list in range (2, 17)
3. In every iteration until we divide first number of a pair by base without remainder unitil is 
equal to zero, at the same time in this while loop we replace the zero in internal list
on the index equal to the remainder of the division with 1.
After we exit while loop, we have list filled with zeros and ones in the index equal to digits in 
given base, we don't care about repetations in one number.
4. Than we create while loop for second number and checks if index equal to b%base==1, if it is
it means there is same digit in both numbers so we return False.
'''

def bases(a, b):
    for i in range(2, 17):
        is_find = True
        arr = [0]*16
        tmp_a, tmp_b = a, b
        while tmp_a != 0:
            arr[tmp_a%i] = 1
            tmp_a //= i
        while tmp_b !=0:
            if arr[tmp_b%i] == 1:
                is_find = False
                break
            tmp_b //= i
        if is_find == True:
            return i
    return False


if __name__ == '__main__':
    # print(is_diff_digits('234175'))
    # print(change_bases(5, 2))
    print(smallest_base(123, 522))

    print(bases(123, 522))