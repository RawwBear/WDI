import math
def f(x):
    return x*math.log(x) - math.log(2020)

def df(x):
    return math.log(x) + 1

def solve():
    x = 1#we start with counting function value for x and our solving method here starts
    eps = 1e-4
    while abs(f(x)) > eps: #abs(f(x)) because the value of the function can be negative
        x = x - f(x)/df(x)#formule for the counting the next intersection with the ox axis from the tangent method
    return x

if __name__ == '__main__':
    print(solve())