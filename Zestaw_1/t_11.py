#zaprzyjaznione liczby to takie ktorych suma dzielinikow jednej bez niej jest rowna drugiej liczbie anlogicznie dla drugiej
#220 = 1 + 2 + 4 + 71 + 142 (dzielniki 284)
#284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 (dzielniki 220)
def divisors(n):
    suma = 0
    for i in range(1, int(n**0.5)+1):#we can find two digits in one looping: 12/6 = 2
        if n%i == 0:
            suma += i
            if i != n//i:
                suma += n//i
    return suma - n

for num1 in range(2, 1000001):
    num2 = divisors(num1)# num2 = divisors of num1 exluding num1
    if num1 == divisors(num2) and num2 < num1: #if num1 = divisors of num2 exluding num2 and numbers are different and same pair isn't print twice
        print(num1, num2)