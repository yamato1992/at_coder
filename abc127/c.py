N, M = map(int, input().split())
l, r = 1, 10 ** 5

for _ in range(M):
    li, ri = map(int, input().split())
    l = max(l, li)
    r = min(r, ri)

ans = r - l + 1 if r >= l else 0
print(ans)