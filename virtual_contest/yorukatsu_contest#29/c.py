n, m = map(int, input().split())
ans = n * m

if n > 1 or m > 1:
    if n >= 2 and m >= 2:
        ans -= 4
    else:
        ans -= 2

if n > 1:
    ans -= max((m - 2) * 2, 0)

if m > 1:
    ans -= max((n - 2) * 2, 0)

print(ans)