from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)

for a in A:
    d[a] += 1

kinds = len(d)
d = sorted(d.items(), key=lambda x: x[1])
ans = 0

for i in range(kinds - k):
    ans += d[i][1]

print(ans)
