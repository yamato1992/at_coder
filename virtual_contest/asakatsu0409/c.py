n, p = map(int, input().split())
a = list(map(int, input().split()))

is_odd = False
for ai in a:
    if ai % 2 == 1:
        is_odd = True
        break

if is_odd:
    ans = 2 ** (n - 1)
else:
    if p == 0:
        ans = 2 ** n
    else:
        ans = 0
print(ans)