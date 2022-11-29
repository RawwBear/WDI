weight_set = [6,2,4,1]
def wrapper(weight_set, mass):
    def check(weight_set,remaining=mass, i=0):
        n = len(weight_set)
        if remaining == 0: return True
        if remaining < 0 or i > n - 1: return False
        return check(weight_set, remaining, i+1) or check(weight_set, remaining - weight_set[i], i+1)
    return check(weight_set)
    #if we took weight from the array the remaings weights to weigh out was decreased by last wieght we took if we didin't
    #take wieight remaings mass to weigh out stays the same
print(wrapper(weight_set))