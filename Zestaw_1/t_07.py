num = int(input("Enter the number you want to check if it is the product of two consecutive numbers in fibonacci sequence: "))
f1, f2 = 1, 1
while f1*f2 < num:
    f1, f2 = f2, f1+f2
if f1*f2 == num:
    print("It is!")
else:
    print("It isn't")