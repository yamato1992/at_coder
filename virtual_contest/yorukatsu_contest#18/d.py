def dfs(x):
    if visited[x]:
        return 
    visited[x] = True
    for i in range(n):
        if graph[x][i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)] 
sides = []

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    sides.append([a, b])
    graph[a][b] = True
    graph[b][a] = True

ans = 0
for side in sides:
    visited = [False] * n
    l, r = side
    graph[l][r] = False
    graph[r][l] = False
    dfs(0)
    if False in visited:
        ans += 1
    graph[l][r] = True
    graph[r][l] = True

print(ans)

