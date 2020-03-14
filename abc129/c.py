N, M = map(int, input().split())
broken_step = [0] * (N + 1)
for _ in range(M):
    n = int(input())
    broken_step[n] = 1

dp = [1] * (N + 1)
dp[1] = 0 if broken_step[1] == 1 else dp[0]

for i in range(2, N + 1):
    if broken_step[i] == 1:
        dp[i] = 0
    else:
        dp[i] = dp[i -1] + dp[i - 2]

print(dp[-1] % 1000000007)
