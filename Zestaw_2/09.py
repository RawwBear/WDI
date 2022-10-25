def metoda_prostokatow(k, n):
    #k - prosta rownolegla do OY ograniczająca pole od prawej strony, n - liczba prostokatow na ktore mam podzielic pole
    pole = 0 #pola wszystkich zsumowanych prostokatow
    x = (k - 1)/n
    mid = (k-1)/(2*n) + 1 #mid - srodek pierwszego prostokata
    y = 1/mid
    pole += x*y
    for _ in range(n-1):
        mid = mid + x
        pole += x * (1/mid)
    return pole

print(metoda_prostokatow(13, 13))
print(metoda_prostokatow(13, 4))
