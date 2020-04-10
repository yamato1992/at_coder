from math import sqrt

n = int(input())
total = 0
p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append([x, y])

for i in range(n - 1):
    for j in range(i, n):
        xi, yi = p[i]
        xj, yj = p[j]
        total += sqrt((xi -xj) ** 2 + (yi - yj) ** 2)

ans = total / n * 2
print(ans)
