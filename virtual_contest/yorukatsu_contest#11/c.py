s = list(input())
n = len(s)
ans = [0] * n
rs = []
ls = []

for i, c in enumerate(s):
    if c == 'R':
        rs.append(i)
    else:
        ls.append(i)

p = 0
for i, l in enumerate(ls):
    ans[l] += (l - p) // 2
    ans[l - 1] += (l - p) // 2
    if (l - p) % 2 == 1:
        ans[l - 1] += 1
    if l + 1 < n:
        p = l + 1

p = n - 1
rs = rs[::-1]
for i, r in enumerate(rs):
    ans[r] += (p - r) // 2
    ans[r + 1] += (p - r) // 2
    if (p - r) % 2 == 1:
        ans[r + 1] += 1
    if r - 1 >= 0:
        p = r - 1

print(*ans) 
