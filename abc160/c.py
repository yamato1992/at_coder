k, n = map(int, input().split())
a = list(map(int, input().split()))
max_dist = 0
for i in range(n):
    dist = (a[(i + 1) % n] - a[i]) % k
    max_dist = max(max_dist, dist)
ans = k - max_dist
print(ans)
