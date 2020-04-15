from math import pi
r, d = map(int, input().split())
area = r ** 2 * pi
circumference = d * 2 * pi
ans = area * circumference
print(ans)