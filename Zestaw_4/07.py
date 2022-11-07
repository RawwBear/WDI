from random import randrange

def type_in(curr_elem, arr2):
    for i in range(len(arr2)):
        if arr2[i] == 0:
            arr2[i] = curr_elem
            return
        else:
            if curr_elem < arr2[i]:
                arr2[i], curr_elem = curr_elem, arr2[i]



def single_num(n):
    arr1 = [sorted([randrange(1, 31) for _ in range(n)]) for _ in range(n)]
    arr2 = [0 for _ in range(n*n)]#create one-dimensial array filled with zeros

    for i in range(n):
        print(arr1[i])

    for i in range(n):
        for j in range(n):
            curr_elem = arr1[i][j]
            type_in(curr_elem, arr2)
    return arr2
if __name__ == '__main__':
    print(single_num(5))