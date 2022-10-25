def change_systems(num, base):
    '''Function takes decimal number as input as wall as base for which we should convert the number then return
     number in choosen system'''
    res = ''
    if base == 10:
        return num
    if base < 10:
        while num!=0:
            res += str(num%base)
            num //= base
        return res[::-1]
    else:
        Letters = ['A', 'B', 'C', 'D', 'E', 'F']
        while num != 0:
            rest = num%base
            if rest > 9:
                rest = rest - 10 #after substraction index of the Letters will be equal to rest value
                res += Letters[rest]
            else:
                res += str(rest)
            num //= base
        return res[::-1]

def change_systems_shorter(num, base):
    '''Function takes decimal number as input as wall as base for which we should convert the number then return
     number in choosen system'''
    res = ''
    if base == 10:
        return num
    else:
        Letters = ['A', 'B', 'C', 'D', 'E', 'F']
        while num != 0:
            rest = num%base
            if rest > 9:
                rest = rest - 10 #after substraction index of the Letters will be equal to rest value
                res += Letters[rest]
            else:
                res += str(rest)
            num //= base
        return res[::-1]

if __name__ == "__main__":
    print(change_systems(23, 12))
    print(change_systems(1238, 15))
