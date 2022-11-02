def factorial(num):
    p = 1
    res = 1
    while p <= num:
        res *= p
        p += 1
    return res

def birthday_paradox(n):
    '''
    We will ignore the leap year for the simplicity's sake. Number n must between 20 and 40 inclusive.
    '''
    omega = 365**n
    opp_a = factorial(365)/(factorial(365-n))
    opp_event = opp_a/omega
    return f'{(1 - opp_event)*100}%'

if __name__ == '__main__':
    print(factorial(5))
    print(birthday_paradox(30))