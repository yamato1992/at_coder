from collections import defaultdict
n = int(input())
h = 'MARCH'
d = [0] * 5
for _ in range(n):
    s = input()
    if s[0] in h:
        d[h.find(s[0])] += 1

ans = 0
for i in range(5):
    for j in range(i, 5):
        if i == j:
            continue
        for k in range(j, 5):
            if i == k or j == k:
                continue
            ans += d[i] * d[j] * d[k]
print(ans)
