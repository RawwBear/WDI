#I use dividing in the bar
def decimal_extension(a, b, n):
    res = str(a//b) + '.'
    if a % b == 0:
        return a/b
    for i in range(n):
        a = (a % b)*10
        res += str(a//b)
    return res

print(decimal_extension(4, 2, 20))