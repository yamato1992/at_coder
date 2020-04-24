from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)

for a in A:
    d[a] += 1

ans = 0
for k, v in d.items():
    ans += (v * (v - 1)) // 2

for i in range(n):
    ai = A[i]
    cnt = d[ai]
    diff = (cnt * (cnt - 1)) // 2 - ((cnt - 1) * (cnt - 2)) // 2
    print(ans - diff)