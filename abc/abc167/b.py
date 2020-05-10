a, b, c, k = map(int, input().split())
ans = 0
ans += min(a, k)
ans -= max(0, k - a - b)
print(ans)