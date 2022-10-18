precision = 0.000000001
volume = int(input("Input number you want to get cube root of: "))
h = volume
b = 1
a = 1
while abs(a-h)>precision:
    h = (a+b+h)/3
    a = (volume/h)**0.5
    b = a
print(a)


