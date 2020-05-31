n, q = map(int, input().split())
edge = [[] for _ in range(n)]
count = [0] * n

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    count[p] += x

not_yet = [True] * n
not_yet[0] = False
stack = [0]
while stack:
    parent = stack.pop()
    for child in edge[parent]:
        if not_yet[child]:
            count[child] += count[parent]
            not_yet[child] = False
            stack.append(child)
print(*count)
    