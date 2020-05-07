n = int(input())
s = list(input())
ans = 0
for i in range(1, n - 1):
    l = set(s[:i])
    r = set(s[i:])
    ans = max(ans, len(l & r))
print(ans)