N = int(input())

dp = [100000 for _ in range(N + 1)]

dp[0] = 0
for n in range(1, N + 1):
    for num in [6, 9]:
        power = 1
        while power <= n: 
            dp[n] = min(dp[n], dp[n - power] + 1)
            power *= num

print(dp[N])
