from math import sqrt
n = int(input())
coordinate = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        xi, yi = coordinate[i]
        xj, yj = coordinate[j]
        line = sqrt(abs(xi - xj) ** 2 + abs(yi - yj) ** 2)
        ans = max(ans, line)
print(ans)