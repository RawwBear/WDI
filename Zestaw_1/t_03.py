
'''
#CREATE SEQUENCE WITHOUT LISTS
seq = str(f1) + ' ' + str(f2) #we need to add separator
print(seq)
while f2 <= num:
    f1, f2 = f2, f1 + f2
    seq = seq + ' ' + str(f2)
print(seq)
'''

num = int(input('Type sum of the subsequence: '))
f1, f2 = 1, 1
seq = [f1, f2]
while f2 <= num:
    f1, f2 = f2, f1 + f2
    seq.append(f2)
print(seq)

#we go by from index 0 and 1 if right + left < num we move right by one index, if right + left > num we move left by one index

left, right = 0, seq[1]
suma = left + right
#suma = sum(seq[left: right+1])

while suma < num:
    right += 1
    suma += seq[right]
    # suma = sum(seq[left: right + 1])
while suma > num:
    suma -= seq[left]
    left += 1
    # suma = sum(seq[left: right + 1])
if suma == num:
    print('Subseq with given sum exist! ')
else:
    print('Subseq doesn\'t\'exist')