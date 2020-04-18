a, b, c = map(int, input().split())

ans = 0
if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
    ans = a * b * c // max(a, b, c)
print(ans)