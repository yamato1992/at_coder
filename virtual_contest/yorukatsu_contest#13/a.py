n, m = map(int, input().split())
l = 1
r = 10 ** 5
for _ in range(m):
    li, ri = map(int, input().split())
    l = max(l, li)
    r = min(r, ri)

print(r - l + 1 if r >= l else 0)
