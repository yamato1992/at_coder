n = int(input())
t = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        x -= 1
        t[i].append([x, y])

ans = 0
for p in range(1 << n):
    cnt = 0
    is_not = False
    for i in range(n):
        if p >> i & 1:
            cnt += 1
            for ti in t[i]:
                x, y = ti
                if (p >> x & 1) != y:
                    is_not = True
                    cnt = 0
                    break
        if is_not:
            break
    ans = max(ans, cnt)
print(ans)
