''''
Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
'''
def determine_e(n):
    #works only form python sets size of digits after comma
    e = 1
    factorial = 1
    i = 1
    digits = []
    while i != n:
        e += 1 / factorial
        # print(e)
        i += 1
        factorial *= i
    return e

def long_dir(a, b, t):
    for i in range(1, len(t)):
        a *= 10
        t[i] += a//b
        a %= b
        if a == 0: return #break function if a == 0

def e_extenstion(n):
    digits = [1] + [0]*(n+10)#we need to have [1] + otherwise our solution will be 1.718... instead of 2.718...
    fact = 1
    k = 1
    while fact <= 10**(n+1):
        fact *= k
        k += 1
        long_dir(1, fact, digits)#change a and t value for us it means that 1 is changed and digits list now will contains decimal extension of 1/fact to n places after comma
    for i in range(len(digits)-1, 0, -1):
        #Wykonuje operacje jak w dodawaniu piesmnym przenosze cyfre o jeden do przodu jezeli liczba jest wieksza niz 9
        digits[i-1] += digits[i]//10
        digits[i] %= 10
    return str(digits[0]) + '.'+ ''.join(map(str, digits[1:n+1]))


def written_div(a, b, array):
    for i in range(1, len(array)):
        a *= 10
        array[i] += a//b #set value for array[i] to result of division a by b
        a %= b #set a as rest of devision a by b
        if a == 0: return #if a == 0 break the programm next values also will be zeros

def e_extension_practise(n):
    digits = [1] + [0]*(n+1)
    fact = 1
    k = 1
    while k <= n+1:
        fact *= k
        k += 1
        written_div(1, fact, digits)#update values in digits list
    for i in range(len(digits)-1, 0, -1):
        digits[i - 1] += digits[i]//10
        digits[i] %= 10
    return f'{digits[0]}.' + ''.join(map(str, digits[1:n+1]))

if __name__ == "__main__":
    print(determine_e(20))
    print(e_extenstion(20)) #2.71828182845904523533