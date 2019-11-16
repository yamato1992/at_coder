N, M = map(int, input().split())
graph = [[False] * N for _ in range(N)]
visited = [False] * N
sides = []


def dfs(node):
    if visited[node]:
        return
    
    visited[node] = True

    for i in range(N):
        if graph[node][i]:
            dfs(i)


for i in range(M):
    a, b = map(int, input().split())
    sides.append([a - 1, b - 1])
    graph[a - 1][b - 1] = True
    graph[b - 1][a - 1] = True

ans = 0
for side in sides:
    visited = [False] * N
    graph[side[0]][side[1]] = False
    graph[side[1]][side[0]] = False
    dfs(0)
    if False in visited:
        ans += 1
    graph[side[0]][side[1]] = True
    graph[side[1]][side[0]] = True

print(ans)
