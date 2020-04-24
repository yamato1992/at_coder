n, k = map(int, input().split())
H = [int(input()) for _ in range(n)]
H.sort()
ans = 10 ** 9
for i in range(n - k + 1):
    hmin = H[i]
    hmax = H[i + k - 1]
    ans = min(ans, hmax - hmin)
print(ans)