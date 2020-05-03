n, w = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(n):
    weight, value = goods[i]
    for sum_w in range(w + 1):
        if (sum_w - weight) >= 0:
            dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w - weight] + value)

        dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w])

print(dp[n][w])