N, K = map(int, input().split())
P = list(map(int, input().split()))

s = sum(P[0:K])
m = s
id = 0
for i in range(1, N - K + 1):
    s += (P[i + K - 1] - P[i - 1])
    if s > m:
        id = i
        m = s

ans = 0
for j in range(id, id + K):
    ans += (P[j] + 1) / 2
print(ans)