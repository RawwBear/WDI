precision = 0.000001
area = int(input("Input number you want to get root of: "))
a = area
b = area / a
while abs(a-b)>precision:
    a = (a+b)/2
    b = area / a
print(a)