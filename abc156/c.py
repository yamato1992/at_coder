import math

N = int(input())
X = list(map(int, input().split()))
max_xi = max(X)
min_xi = min(X)
ans = int(math.pow(99, 2)) * 100
for p in range(min_xi, max_xi + 1):
    total = 0
    for xi in X:
        total += int(math.pow(xi - p, 2))
    ans = min(ans, total)
print(ans)