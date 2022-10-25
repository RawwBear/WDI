def divasors_with_smallest_diff(num):
    diff_mini = num+1
    for i in range(int(num**0.5) + 1, 1, -1):#we start from the end to find faster divisors with smallest diff
        if num%i == 0:
            sec_div = num//i
            if abs(sec_div - i) < diff_mini:#first pair will be answer because we start with the bigesst divisors
                diff_mini = abs(sec_div - i)
                return i, sec_div

print(divasors_with_smallest_diff(120))
print(divasors_with_smallest_diff(400))

