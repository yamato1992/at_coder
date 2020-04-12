def lucas_number(x):
    if x == 0:
        return 2
    if x == 1:
        return 1
    l = 2
    r = 1
    while x - 1 > 0:
        l, r = r, l + r
        x -= 1
    return r

n = int(input())
print(lucas_number(n))
