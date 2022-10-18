year = 2022
suma = 2023
prev = 0
pair = (0, year)
#We can optimalize end of the range
for x in range(year//2, year):#we can end iteration on 2021 because mini sum for 2022 + 0 is 2022
    prev = year - x
    while x > prev:
        tmp = prev
        prev = x - prev
        x = tmp
    if x + prev < suma:
        suma = x + prev
        pair = (x, prev)
print(suma, pair)































