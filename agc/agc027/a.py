n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
total = sum(a)
ans = 0
if x == total:
    ans = n
elif x > total:
    ans = n - 1
else:
    for v in a:
        x -= v
        if x < 0:
            break
        ans += 1
print(ans)