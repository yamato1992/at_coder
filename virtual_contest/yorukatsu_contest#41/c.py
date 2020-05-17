import math
a, b, x = map(int, input().split())
if x * 2 >= a ** 2 * b:
    ret = (b - x / a ** 2) * 2 / a
else:
    ret = a * b ** 2 / (2 * x)
print(math.degrees(math.atan(ret)))