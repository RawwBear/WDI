def have_common_digits(x, y, base):
    D = [False]*base
    #create a list of length equal to choosen system base, because there is limit to as many digits as many
    #remainder of the devision possible
    while x != 0:
        rest = x%base
        D[rest] = True
        x //= base
    while y != 0:
        rest = y%base
        if D[rest]:
            return True
        y //= base
    return False

# def smallest_base(a, b):
#     for i in range(2, 17):
#         if have_common_digits(a,b,i):
#             return i
#     return False

if __name__ == '__main__':
    a, b = int(input("Give me a: ")), int(input("Give me b: "))
    for i in range(2, 17):
        if have_common_digits(a, b, i) == False:
            print(i)
            break
    else:
        print("Such as base doesn't exist!")