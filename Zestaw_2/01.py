num = int(input("Enter the number for which you want to check if it is the product of any two numbers in fibonacci sequence: "))
f1, f2 = 1, 1
Fibo = [1, 1]
flag = False
while f2 < num:
    f1, f2 = f2, f1+f2
    Fibo.append(f2)
print(Fibo)
for i in Fibo:
    if num % i == 0:#I need to check if result is present in fibonacci sequence
        res = num / i

        for j in Fibo[::-1]:
            if j == res:
                flag = True
                break
if flag == True:
    print("Yes")
else:
    print("No")

#Attempt to solve problem without lists
# f1, f2 = 1, 1
# flag = False
# while f2 < num:
#     f1, f2 = f2, f1 + f2
#     if num % f2 == 0:#I need to check if result is present in fibonacci sequence
#         a, b = f1, f2
#         res = num / f2
#         if res == 1:
#             flag = True
#             break
#         while f2 < res:
#             f1, f2 = f2, f1 + f2
#         if num == res:
#             flag = True
#             break
#         f1, f2 = a, b
# if flag == True:
#     print("Yes")
# else:
#     print("No")
