import math

def get_leng(num):
    #return lenght of the number
    return math.floor(math.log10(num)) + 1

def create_numbers(num):
    tab = []
    prev_rest = 0
    i = 0
    while get_leng(num) != 1:
        rest, cur_num = num%10, num//10
        tab.append(cur_num)
        tab.append(rest)
        if i != 0:
            tab.append(str(cur_num)+str(prev_rest))
            tab.append(str(rest)+str(prev_rest))
        new_num = str(cur_num) + str(rest)
        tab.append(int(new_num))
        prev_rest = rest
        num //= 10
        i += 1
    return tab


if __name__ == '__main__':
    print(get_leng(1238))
    print(create_numbers(2315))


