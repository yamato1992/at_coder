import math

N, D = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        total = 0
        for (y, z) in zip(x[i], x[j]):
            total += abs(y - z) ** 2
        dist = math.sqrt(total)
        if dist.is_integer():
            cnt += 1

print(cnt)