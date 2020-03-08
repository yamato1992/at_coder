N, K = map(int, input().split())
num = N
ans = 0
while True:
    num //= K
    ans += 1
    if num == 0:
        break
print(ans)