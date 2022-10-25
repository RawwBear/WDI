def sito_erastotenesa(n):
    arr = [0 for _ in range(n+1)]
    primes = []
    p = 2
    while p <= int(n**0.5)+ 1:
        next = 0#next prime number <= int(n**0.5) + 1
        for i in range(p, len(arr)):
            if i%p == 0 and i != p:#index of the array is divided by p and index isn't equal to prime number we divide by
                arr[i] = 1
            if i%p != 0 and next == 0:
                next = i
        p = next
    for i in range(2, len(arr)):
        if arr[i] != 1:
            primes.append(i)
    return primes

if __name__ == "__main__":
    print(sito_erastotenesa(100))