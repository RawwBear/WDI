def nwd(a,b):
    while b!=0:
        a, b = b, a%b
    return a
def nww(a,b):
    return int((a*b)/nwd(a,b))

def add(num1, num2):
    a, b = num1[0], num1[1]
    c, d = num2[0], num2[1]
    mianownik = nww(b,d)
    multi = 1
    a, c = (mianownik/b) * a, (mianownik/d)*c
    licznik = int(a + c)
    return f'{licznik}/{mianownik}'
print(add((1,2), (8,9)))

def subtract(a, b, c, d):
    mianownik = nww(b,d)
    multi = 1
    a, c = (mianownik/b) * a, (mianownik/d)*c
    licznik = int(a - c)
    return f'{licznik}/{mianownik}'
print(subtract(3,7,1,2))

def multiply(a, b, c, d):
    licznik, mianownik = a*c, b*d
    return f'{licznik}/{mianownik}'

print(multiply(1,2,3,7))

def devide(a, b, c, d):
    licznik, mianownik = a*d, b*c
    return f'{licznik}/{mianownik}'
print(devide(1,2,4,5))

def simplify(fraction:tuple):
    div = nwd(fraction[0], fraction[1])
    return f'{int(fraction[0]/div)}/{int(fraction[1]/div)}'
print(simplify((15,40)))