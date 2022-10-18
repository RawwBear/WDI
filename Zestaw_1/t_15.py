from math import sqrt
pi = 1
epsilon = 0.0000001
a = sqrt(0.5)
product = 1
i=1
while i < 6:
    product *= a
    pi = 2/(product)
    a = sqrt(0.5 + 0.5*a)
    i += 1
print(pi)