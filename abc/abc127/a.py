A, B = map(int, input().split())
ans = B
if A <= 12:
    ans //= 2
if A <= 5:
    ans = 0
print(ans)