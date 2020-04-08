N = int(input())
ans = 0
btc = 380000
for _ in range(N):
    x, u = input().split()
    x = float(x)
    ans += x if u == 'JPY' else x * btc
print(ans)