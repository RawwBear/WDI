stop = False
weight_set = [6,4,3,2,1]
with_mass, w_empty = [], []
def wrapper(weight_set, mass):
    def check(weight_set,with_mass=[], w_empty=[], remaining=mass, i=0):
        n = len(weight_set)
        global stop
        if stop: return False
        if remaining == 0:
            stop = True
            print(with_mass, w_empty)
            return True
        if remaining < 0 or i > n - 1: return False
        return check(weight_set,with_mass,w_empty, remaining, i+1) or\
               check(weight_set,with_mass, w_empty + [weight_set[i]],remaining - weight_set[i], i+1)\
               or check(weight_set,with_mass + [weight_set[i]], w_empty, remaining + weight_set[i], i+1)
    return check(weight_set)
    #if we took weight from the array the remaings weights to weigh out was decreased by last wieght we took if we didin't
    #take wieight remaings mass to weigh out stays the same
print(wrapper(weight_set,9))