from math import sqrt
s = int(input())
a = 10 ** 9
b = s // a
c = s % a
if c != 0:
    b += 1
    c = a - c
print(0, 0, a, 1, c, b)