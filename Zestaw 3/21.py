def nwd3(a, b, c):
    #if b > a in first conversion a and b swap values
    for i in range(2):
        while b !=0:
            a, b = b, a%b
        b = c
    return a
print(nwd3(8,12, 40))

def trojki():
    T = [18, 6, 8, 4, 17, 2, 9, 14]
    find_threes = 0
    for i in range(len(T)-3):
        #for every i we need to consider 3 cases e.g. [9, 2, 5, 4], possible threes: (9, 2, 5), (9, 2, 4), (9, 5, 4) for
        #them we need to check ned condition
        seq = T[i+1:i+4] #we always need to choose two digits from this sequence
        for j in range(3):
            two_elem = seq.copy()
            two_elem.pop(j)
            if nwd3(T[i],two_elem[0], two_elem[1]) == 1:
                find_threes += 1
    return find_threes


if __name__ == '__main__':
    print(trojki())
