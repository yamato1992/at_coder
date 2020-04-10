n, m = map(int, input().split())
relation = [1 << i for i in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    relation[x] += 1 << y
    relation[y] += 1 << x

ans = 1
for p in range(1, 1 << n):
    cnt = 0
    for i in range(n):
        if p >> i & 1 and  (relation[i] & p) == p:
            cnt += 1
    ans = max(ans, cnt)

print(ans)