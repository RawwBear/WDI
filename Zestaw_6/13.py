def print_splits(num:int, j:int, split:list[int]):
    if num == 0:
        print(split)
        return

    for i in range(split[j-1], n+1):
        split[j] = i
        print_splits(num-i, j+1, split)
        split[j] = 0