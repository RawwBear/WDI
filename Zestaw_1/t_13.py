a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
i = 2
product = 1#all divisors
while a!= 1:
    if a < b:#the greater number need to be in smallest multiple
        result = b
        while a != 1:#while smaller number is different than 1
            while a % i == 0:#if a if divisible without reminder
                a /= i
                product *= i
                if b % product != 0:#if larger number isn't divisiable by divisor in certain power then multiply result by i
                  result *= i
            product = 1
            i += 1
    else:
        a, b = b, a
i = 2
while c != 1:
    product = 1
    if c < result:
        while c != 1:
            while c % i == 0:
                c /= i
                product *= i
                if result % product != 0:
                    result *= i
            product = 1
            i += 1
    else:
        c, result = result, c

print(result)