def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return 0
    elif a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a+b+c
# this should be a branch edit

