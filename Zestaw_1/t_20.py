a = int(input("Enter the first word of the geometric sequence: "))
b = int(input("Enter the first word of the arithmetic sequence: "))
precision = 0.000000001
while abs(a-b) > precision:
    a_next = (a*b)**0.5
    b_next = (a+b)/2
    a, b = a_next, b_next
print(a)