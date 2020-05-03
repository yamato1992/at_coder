n = int(input())
scaffold = list(map(int, input().split()))
dp = [10 ** 4 * 10 ** 5] * n
dp[0] = 0
dp[1] = abs(scaffold[0] - scaffold[1])

for i in range(2, n):
    cost_1 = abs(scaffold[i - 1] - scaffold[i]) + dp[i - 1]
    cost_2 = abs(scaffold[i - 2] - scaffold[i]) + dp[i - 2]
    dp[i] = min(dp[i], cost_1, cost_2)
    
ans = dp[-1]
print(ans)
