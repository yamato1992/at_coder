x = int(input())

if x % 11 == 0:
    ans = x // 11 * 2
else:
    if x % 11 <= 6:
        ans = x // 11 * 2 + 1
    else:
        ans = (x // 11 + 1) * 2

print(ans)
