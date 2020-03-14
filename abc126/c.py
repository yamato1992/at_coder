N, K = map(int, input().split())
ans = 0
for n in range(1, N + 1):
    p = 1
    x = n
    while x < K:
        p *= 0.5
        x *= 2
    ans += p / N
print(ans)