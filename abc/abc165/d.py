from math import floor
a, b, n = map(int, input().split())
x = min(b - 1, n)
ans = floor(a * x / b) - a * floor(x / b)
print(ans)
