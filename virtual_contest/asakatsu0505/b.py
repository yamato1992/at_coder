x = int(input())
ans = 1
for b in range(2, int(x ** 0.5) + 1):
    p = 1
    while b ** p <= x:
        p += 1
    ans = max(ans, b ** (p -1))
print(ans)
