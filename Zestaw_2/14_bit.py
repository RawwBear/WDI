import math
def mix_numbers(a:int, b:int, mask:int):
    '''
    Create binary mask by taking first possible digit from the first number(a) if mask%2 == 0 else taking first possible
    digit from second number(b). Taking first possible number make us sure that we don't change the order in which the digits
    are arranged in original a and b number (condition for this exercise).
    '''
    new_num = 0
    mult = 1
    while mask > 0 or a > 0: #because mask can start from zero
        if mask%2 == 0:
            d = a%10
            a //= 10
        else:
            d = b%10
            b //= 10
        mask //= 2
        new_num = d*mult + new_num#we add new digits to left side because we take last digits when we divide by 10
        mult *=10
    return new_num

def get_leng(num):
    #e.g. log10^2 = 2, where len(100) = 3
    return math.floor(math.log10(num))+ 1

def validate_mask(a:int, b:int, mask:int):
    cnt1, cnt2 = get_leng(a), get_leng(b)
    #a is represented by 0 in the mask, b as 1
    while mask > 0:
        #we subtract one untill len(a+b) != mask, length of the mask need to be equal to lenght of the sum a+b
        #but we need to take into consideration situation WHEN MASK IS LONGER THAN SUM(a,b) then e.g. a=12, b=345,
        #mask=int('011001',2)=23, then result can be 134205 extra 0 in the number
        if mask%2==0:
            cnt1 -= 1
        else:
            cnt2 -= 1
        mask //= 2
    return cnt1 >=0 and cnt2==0#return True or False depending on whether the conditions are met(subject on conditions)

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i < int(num**(0.5))+1:
        if num % i == 0: return False
        i += 2
        if num % i == 0: return False
        i += 4
    return True

if __name__ == '__main__':
    print(mix_numbers(135, 24, int('011001', base=2)))
    cnt = 0
    cnt2=0
    a, b = map(int, input().split())
    #for loop generate possible masks
    for mask in range(2**(get_leng(a)+get_leng(b))):#the interval depends on the length of the sum a+b in binary system
        if validate_mask(a,b,mask):
            print(mix_numbers(a,b,mask))
            if is_prime(mix_numbers(a,b, mask)):
                cnt += 1
    print(cnt)


