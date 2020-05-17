import math

a, b, h, m = map(int, input().split())
A = (h * 60 + m) * 360 / (12 * 60)
B = 6 * m
C = abs(A - B)

c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C))) ** 0.5
print(c)