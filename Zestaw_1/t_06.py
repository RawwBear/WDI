i = 2
while i**i < 2020:
    i += 1
right = i
left = i-1
precision = 000000.1
while abs(right-left) > precision:
    mean = (right+left)/2
    if mean**mean > 2020:
        right = mean
    else:
        left = mean
print(right)