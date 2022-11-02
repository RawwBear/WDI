def same_digits(num1, num2):
    digits = [0 for _ in range(10)]#create arrays filled with zeros, where idex is eaqual to digit in a number
    #we will be adding or subtracting 1 to array in a place where index = digit in a number
    #after operation we will chack if array is the same as at the start (filled only with zeros)

    while num1 != num2:#if length of both numbers is different they can't have the same digits in the same amount
        digits[num1%10] += 1
        digits[num2%10] -= 1
        num1 //= 10
        num2 //= 10
    if digits == [0 for _ in range(10)]:
        return True
    else:
        return False

print(same_digits(123,231))
print(same_digits(123, 870))
print(same_digits(456, 4456))
print()