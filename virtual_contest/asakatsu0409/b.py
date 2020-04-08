s = list(input())
n = len(s) + 1

l = [0] * n
r = [0] * n

for i, c in enumerate(s, 1):
    if c == '>':
        l[i] = 0
    else:
        l[i] = l[i - 1] + 1

for i, c in enumerate(s[::-1]):
    i = n - 2 - i
    if c == '<':
        r[i] = 0
    else:
        r[i] = r[i + 1] + 1

seq = [x if x > y else y for x, y in zip(l, r)]

ans = sum(seq)
print(ans)
    