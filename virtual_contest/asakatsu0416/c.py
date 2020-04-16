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

for i in range(n - 2):
    for j in range(i, n - 1):
        if s[i] == s[j]:
            continue
        k = 2 * j - i
        if k >= n:
            continue
        if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            ans -= 1
print(ans)