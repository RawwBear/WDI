f1 = int(input("Enter first number in the sequence: "))
f2 = int(input("Enter second number in the sequence: "))
precision = 0.000001
quotient, last_quotient = 1, 2
while abs(last_quotient - quotient) > precision:
    last_quotient = f1/f2
    f1, f2 = f2, f1+f2
    quotient = f1/f2
#I want to print 3 first digits after comma
print(round(quotient, 3))

