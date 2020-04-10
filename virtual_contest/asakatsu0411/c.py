from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    a = int(input())
    d[a] += 1

ans = 0
for v in d.values():
    if v % 2 == 1:
        ans += 1

print(ans)