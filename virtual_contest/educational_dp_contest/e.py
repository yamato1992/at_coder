n, w = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(n)]
dp = [[10 ** 11] * (10 ** 5 + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    weight, value = goods[i]
    for sum_value in range(10 ** 5 + 1):
        if (sum_value - value) >= 0:
            dp[i + 1][sum_value] = min(dp[i + 1][sum_value], dp[i][sum_value - value] + weight)
        dp[i + 1][sum_value] = min(dp[i + 1][sum_value], dp[i][sum_value])

ans = 0
for sum_value in range(10 ** 5 + 1):
    if dp[n][sum_value] <= w:
        ans = sum_value

print(ans)