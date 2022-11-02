import math
def get_leng(num):
    return math.floor(math.log10(num))+1
print(get_leng(2315))

#cross out digit when 0 in mask, if 1 digit stay
def cross_out(num:int, mask:int):
    multi = 1
    new_num = 0
    while mask != 0:
        if mask%2 ==1:
            digit = num%10
            new_num = digit*multi + new_num
            multi *= 10
        num //= 10
        mask //= 2
    return new_num


if __name__ == '__main__':
    counter = 0
    num = int(input("Enter the number: "))
    for mask in range(1, 2**get_leng(num)):#we start from 1 because for mask 0 there is no number
        new_num = cross_out(num, mask)
        if new_num%7 ==0:
            print(new_num)
            counter += 1
    print(counter)