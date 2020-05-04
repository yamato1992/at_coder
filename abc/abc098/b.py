n = int(input())
s = list(input())
ans = 0

for i in range(1, n - 1):
    x = set(s[:i])
    y = set(s[i:])
    ans = max(ans, len(x & y))

print(ans)