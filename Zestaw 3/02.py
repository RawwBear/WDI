def sort_ascending(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
def is_same_digits_in_number(num1, num2):
    arr_1 = [int(i) for i in str(num1)]#create lists contains digits then sort them and compare if are the same
    arr_2 = [int(i) for i in str(num2)]
    if sort_ascending(arr_1) == sort_ascending(arr_2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_same_digits_in_number(123, 321))
    print(is_same_digits_in_number(1255, 5125))
    print(is_same_digits_in_number(1222222, 12))
    print(sort_ascending([2,4,1,0,5]))