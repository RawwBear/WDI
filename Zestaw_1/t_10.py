#Perfect number - num of positive factors exluding itself is equal to this numver as 6 = 1+2+3
suma = 0
n = int(input("Input the number: "))
for i in range(1, int(n**0.5)+1):#we can find two digits in one looping: 12/6 = 2
    if n%i == 0:
        suma += i
        if i != n//i:
            suma += n//i
if suma - n == n:
    print("That's perfect number")
else:
    print("That's not a perfect number")

