from collections import defaultdict

n = int(input())
d = defaultdict(int)

ans = 0
for _ in range(n):
    a = int(input())
    d[a] += 1
    if d[a] > 1:
        ans += 1
print(ans)
