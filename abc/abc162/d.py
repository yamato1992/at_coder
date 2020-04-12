n = int(input())
s = list(input())
r = 0
g = 0
b = 0
for c in s:
    if c == 'R':
        r += 1
    elif c == 'G':
        g += 1
    else:
        b += 1

ans = r * g * b

for i in range(n - 1):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            continue
        k = j * 2 - i
        if k >= n or s[k] == s[i] or s[k] == s[j]:
            continue
        ans -= 1

print(ans)
