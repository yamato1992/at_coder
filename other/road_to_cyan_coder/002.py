n = int(input())
ans = 0
for i in range(1, n + 1, 2):
    m = 1
    num = i
    for j in range(2, n + 1):
        cnt = 0
        while num % j == 0:
            num //= j
            cnt += 1
        m *= (cnt + 1)
    if m == 8:
        ans += 1
print(ans)
