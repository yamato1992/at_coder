n, k = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    j = 17
    while i * 2 ** j >= k and j >= 0:
        j -= 1
    ans += 1 / n * (1 / 2) ** (j + 1)
print(ans)
