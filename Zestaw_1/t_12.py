# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

#Fancy way for input, not faster at all xd
dict = {}
for i in [chr(j).lower() for j in range(65, 68)]:
    dict[i] = int(input("Enter the number:"))
print(dict)
a = dict['a']
b = dict['b']
c = dict['c']

#1
while a != b:
    if a > b:
        a, b = b, a-b
    else:
        a, b = b-a, a

while a != c:
    if a > c:
        a, c = c, a - c
    else:
        a, c = c - a, a
print(a)

#2
def nwd(a, b):
    while a != b:
        if a > b:
            a, b = b, a - b
        else:
            a, b = b - a, a
    return a

print(nwd(nwd(a,b),c))

