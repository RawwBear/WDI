def ractangle_method(k):
    x = 1
    eps = 1e-6
    area = 0
    while x < k:
        area += (1/x)*eps
        x += eps
    return area

print(ractangle_method(20))