'''
Program need to return 10th largest unique value. User enters numbers untill he enters zero which means
end of the sequence entry.
'''
def type_in(arr, num):
    for i in range(len(arr)):
        if num > arr[i]:
            num, arr[i] = arr[i], num
        elif num == arr[i]:#prevent type in repeated values
            break
    return arr

if __name__ == "__main__":
    arr = [0 for _ in range(10)]#create array filled with zeros
    num = 1
    while num != 0:
        num = int(input("Enter the number: "))
        arr = type_in(arr, num)
    print(arr)
    print(arr[9])
