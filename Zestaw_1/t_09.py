#hehe I did decomposition into prime numbers
n = int(input("Input the number: "))
print(1)
i = 2
while n > 0:
    if n%i == 0:
        print(i)
        while n%i == 0:
            n //= i
    i += 1

#and now the right task, find all divisors for given number
n = int(input("Input the number: "))
for i in range(1, int(n**0.5)+1):#we can find two digits in one looping: 12/6 = 2
    if n%i == 0:
        print(i)
        if i != n//i:
            print(n//i)
