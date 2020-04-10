n, q = map(int, input().split())
node = [[] for _ in range(n)]
ans = [0] * n

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)

for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x

not_yet = [True] * n
not_yet[0] = False
stack = [0]
while stack:
    parent = stack.pop()
    for child in node[parent]:
        if not_yet[child]:
            ans[child] += ans[parent]
            not_yet[child] = False
            stack.append(child)

print(*ans)
