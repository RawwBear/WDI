precision = int(input("Enter the precision you want to know e number: "))
e = 1
factorial = 1
i = 1
while i != precision:
    e += 1/factorial
    i += 1
    factorial *= i
print(e)