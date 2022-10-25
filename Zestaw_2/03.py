def change_system(num, base):
    res = ''
    while num != 0:
        res += str(num % base)
        num //= base
    return res[::-1]

def is_palindrom(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[-i - 1]:
            return False
    return True

num = 5
print(change_system(2, 2))
print(is_palindrom(num))#return True is decimal number is palindrom
print(is_palindrom(change_system(num, 2)))#retun True if binary number is palindrom

