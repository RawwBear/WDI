
n = int(input("Input number: "))
is_prime = True
if n < 2:
    is_prime = False
for i in range(2, int(n**0.5)+1):
    if n%i == 0:
        is_prime = False
        break
if is_prime == True:
    print("That's prime number")
else:
    print("That's not a prime number")