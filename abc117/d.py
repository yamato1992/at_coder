n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
x = 0
for i in range(40, -1, -1):
    c = 0
    for ai in a:
        if (ai >> i) & 1:
            c += 1
    if (n - c) > c and x + (1 << i) <= k:
        x += 1 << i
        ans += (n - c) * (1 << i)
    else:
        ans += c * (1 << i)
print(ans)