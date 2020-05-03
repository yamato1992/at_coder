n, k = map(int, input().split())
scaffolds = list(map(int, input().split()))
dp = [10 ** 5 * 10 ** 4] * n
dp[0] = 0
for i in range(n):
    for j in range(1, k + 1):
        if i + j >= n:
            break
        dp[i + j] = min(dp[i + j], abs(scaffolds[i] - scaffolds[i + j]) + dp[i])
print(dp[-1])