def all_n_power_numbers(n):
    first = 0
    i = 1
    for _ in range(n):#find smallest n-digit number
        first += 1*i
        i *= 10
    last = 0
    i = 1
    for _ in range(n):#find largest n-digit number
        last += 9*i
        i *= 10
    while first <= last:#while number have n digits
        suma = 0
        first += 1
        curr = first
        while curr != 0:
            rest = curr%10
            power = rest
            for _ in range(n-1):#pow(rest, n) by iteration
                rest *= power
            suma += rest
            curr //= 10
        if suma == first:
            print(first)

print(all_n_power_numbers(4))

