s = list(input())
n = len(s)
ans = 0
ans += n - 1
ans += n - 1
for i in range(1, n - 1):
    if s[i] == 'U':
        ans += n - (i + 1)
        ans += i * 2
    else:
        ans += (n - (i + 1)) * 2
        ans += i
print(ans)