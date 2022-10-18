num2 = int(input())
root = 0
x = 1
suma = 0
while suma + x <= num2:#we have to add x to get the root for the sum be correct
    suma += x
    x += 2
    root += 1
print(root)