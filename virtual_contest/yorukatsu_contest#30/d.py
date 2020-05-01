from math import ceil
n, h = map(int, input().split())
cut = set()
throw = []

for _ in range(n):
    a, b = map(int, input().split())
    cut.add(a)
    throw.append(b)

throw.sort(reverse=True)
ans = 0
m_cut = max(cut)

for t in throw:
    if t > m_cut:
        ans += 1
        h -= t
    if h <= 0:
        break

if h > 0:
    ans += ceil(h / m_cut)

print(ans)