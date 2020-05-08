n, m = map(int, input().split())
results = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(m - 1):
    for j in range(i + 1, m):
        points = 0
        for k in range(n):
            points += max(results[k][i], results[k][j])
        ans = max(ans, points)
print(ans)