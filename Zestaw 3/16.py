from random import randrange
n = int(input("Enter size of the list: "))
array = [randrange(-10, 11) for _ in range(n)]
print(array)
def bigest_and_smallest():
    max_elem, min_elem = array[0], array[0]
    max_counter, min_counter = 1, 1
    for i in range(1, len(array)):
        if array[i] == max_elem:
            max_counter += 1
        elif array[i] == min_elem:
            min_counter += 1
        elif array[i] > max_elem:
            max_elem = array[i]
            max_counter = 1
        elif array[i] < min_elem:
            min_elem = array[i]
            min_counter = 1
    if min_counter > 1 or max_counter > 1:
        return False
    else: return True

def big_and_small_short():
    return array.count(max(array)) == array.count(min(array)) == 1

if __name__ == '__main__':
    print(bigest_and_smallest())
    print(big_and_small_short())