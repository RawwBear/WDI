#!/bin/env python
#zestaw 2 - rekurencje
def genNum(n1, n2, cur=0):
    pr = True
    if n1 != 0:
        genNum(n1//10, n2, cur*10+n1%10)
        pr = False
    if n2 != 0:
        genNum(n1, n2//10, cur*10+n2%10)
        pr = False
    if pr:
        print(cur)


def rev(n):
    m = 0
    while n > 0:
        m = m*10+n%10
        n //= 10
    return m


n1 = rev(int(input()))
n2 = rev(int(input()))

genNum(n1, n2)
