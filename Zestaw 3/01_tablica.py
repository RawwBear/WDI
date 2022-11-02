def change(num, base):
    signs = '0123456789ABCDEF'
    res = ''
    while num != 0:
        rest = num%base
        for i in range(16):
            if i == rest:
                res = signs[i] + res#I insert from the left to avoid having to reverse the number
        num //= base
    return res


print(change(12, 16))