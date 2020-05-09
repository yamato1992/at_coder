n, m = map(int, input().split())
swtiches = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
ans = 0

for i in range(2 ** n):
    is_on = True
    for j in range(m):
        k = swtiches[j][0]
        s = swtiches[j][1:]
        cnt = 0
        for si in s:
            if i >> (si - 1) & 1:
                cnt += 1
        if cnt % 2 != p[j]:
            is_on = False
    if is_on:
        ans += 1

print(ans)