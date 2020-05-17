n, m = map(int, input().split())
node = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)

ans = [-1] * n
ans[0] = 0
stk = [[0] + node[0]]

while stk:
    s = stk.pop(0)
    fr = s[0]
    for i in s[1:]:
        if ans[i] == -1:
            ans[i] = fr + 1
            stk.append([i] + node[i])

if -1 in ans:
    print('No')
else:
    print('Yes')
    for i in range(1, n):
        print(ans[i])
