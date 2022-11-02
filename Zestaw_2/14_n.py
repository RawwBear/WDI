import random

def mix(a:int, b:int):
    tab_a = [0]*len(str(a))
    tab_b = [0]*len(str(b))
    i = len(str(a))-1
    while a!= 0:
        tab_a[i] = a%10
        i -= 1
        a //=10
    i = len(str(b))-1
    while b!= 0:
        tab_b[i] = b%10
        i -= 1
        b //=10
    res=[]
    multi = 1
    while len(tab_a) != 0 or len(tab_b) !=0:
        if len(tab_a) == 0:
            choosen_list = tab_b
        elif len(tab_b) == 0:
            choosen_list = tab_a
        else:
            choosen_list =random.choice([tab_a, tab_b])
        res.append(choosen_list[0])
        if choosen_list == tab_b:
            del tab_b[0]
        else:
            del tab_a[0]
    print(res)
    print(tab_a, tab_b)
print(mix(123,45))




