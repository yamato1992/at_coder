n = int(input())
pillars = []
for _ in range(n):
    x, y = map(int, input().split())
    pillars.append((x, y))
pillars.sort()
points = set(pillars)
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = pillars[i]
        x2, y2 = pillars[j]
        x3 = x2 + y2 - y1
        y3 = y2 + x1 - x2
        x4 = x1 + y2 - y1
        y4 = y1 + x1 - x2
        if (x3, y3) in points and (x4, y4) in points:
            ans = max(ans, (x1 - x2) ** 2 + (y1 - y2) ** 2)

print(ans)