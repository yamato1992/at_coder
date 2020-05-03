n, m = map(int, input().split())
height = list(map(int, input().split()))
roads = [[] for _ in range(n)]
checked = [1] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    roads[a].append(b)
    roads[b].append(a)

ans = 0
for i in range(n):
    if checked[i] == 0:
        continue
    for road in roads[i]:
        if height[i] > height[road]:
            checked[road] = 0
        else:
            checked[i] = 0

print(sum(checked))