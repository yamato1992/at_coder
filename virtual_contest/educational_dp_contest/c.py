n = int(input())
acts = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
a, b, c = acts[0]
dp[0] = [a, b, c]
for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + acts[i][j])
print(max(dp[-1]))