def is_multiple_expr(num):
    a = 2
    while a <= num:
        if num % a == 0:
            return True
        a = 3*a + 1
        print(a)
    return False

print(is_multiple_expr(31))