def disconti_num_fibo(num):
    f1, f2 = 1, 1
    suma = 2
    fibo = [f1, f2]
    while f2 < num and suma < num:
        f1, f2 = f2, f1+f2
        suma += f2
        fibo.append(f2)
    idx = 0
    while suma > num:
        suma -= fibo[idx]
        idx += 1
    if suma != num:
        return False
    return True
# print(disconti_num_fibo(1))

if __name__ == '__main__':
    num = int(input("Enter the number: "))
    while True:
        num += 1
        if disconti_num_fibo(num) == False:
            print(num)
            break
