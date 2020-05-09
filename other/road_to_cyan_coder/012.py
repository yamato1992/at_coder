n, m = map(int, input().split())
relation = [1 << i for i in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    relation[x] += 2 ** y
    relation[y] += 2 ** x

ans = 0
for i in range(1, 2 ** n):
    is_match = True
    cnt = 0
    for j in range(n):
        if i >> j & 1:
            if relation[j] & i == i:
                cnt += 1
                continue
            else:
                is_match = False
                break
    if is_match:
        ans = max(ans, cnt)
print(ans)