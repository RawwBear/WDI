from random import sample
def are_chessing_each_other(n):#n - number of hetmans on the board
    x_cords = sample(range(0,100), n)
    y_cords = sample(range(0, 100), n)
    dane = [(x_cords[i], y_cords[i]) for i in range(n)]#contain coordinates of hetman location
    print(dane)


print(are_chessing_each_other(4))