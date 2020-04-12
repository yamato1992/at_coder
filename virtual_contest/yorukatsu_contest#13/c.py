from math import ceil
n, k = map(int, input().split())
nums = list(map(int, input().split()))
same = k
ans = 1
if same < n:
    ans += ceil((n - same) / (k - 1))
print(ans)
