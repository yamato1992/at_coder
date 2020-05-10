n, m, x = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]
books.sort()

stk = [[0 for _ in range(m + 1)]]
for i in range(n):
    cost = books[i][0]
    effect = books[i][1:]
    for j in range(len(stk)):
        sc = stk[j][0]
        tmp = []
        for k in range(m):
            tmp.append(effect[k] + stk[j][k + 1])
        stk.append([sc + cost] + tmp)

stk.sort()

for s in stk:
    cost = s[0]
    eff = s[1:]
    is_ok = True
    for e in eff:
        if e < x:
            is_ok = False
            break
    if is_ok:
        print(cost)
        exit()
print(-1)