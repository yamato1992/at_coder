def make_arr(x, arr):
    if len(arr) == n:
        pattern.append(arr)
    else:
        for i in range(x, m + 1):
            make_arr(i, arr + [i])

n, m, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]
pattern = []

for i in range(1, m + 1):
    make_arr(i, [i])

ans = 0
for p in pattern:
    point = 0
    for a, b, c, d in query:
        a -= 1
        b -= 1
        if  (p[b] - p[a]) == c:
            point += d
    ans = max(ans, point)
print(ans)
