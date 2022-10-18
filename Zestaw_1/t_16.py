
starter_word = 0
max_steps = 0
for a_start in range(2, 10_001):
    a = a_start
    steps = 0
    while a != 1:
        a = (a%2)*(3*a+1) + (1-a%2)*(a/2)
        steps += 1
    if steps > max_steps:
        max_steps = steps
        starter_word = a_start
print(max_steps, starter_word)
