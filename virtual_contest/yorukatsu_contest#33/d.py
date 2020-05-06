n = int(input())
dp = [10 ** 5 for _ in range(n + 1)]

dp[0] = 0
for i in range(1, n + 1):
    for num in [6, 9]:
        power = 1
        while power <= i:
            dp[i] = min(dp[i], dp[i - power] + 1)
            power *= num

print(dp[n])