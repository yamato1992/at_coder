from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
ans = defaultdict(int)

for a in A:
    ans[a - 1] += 1

for i in range(n):
    print(ans[i])

