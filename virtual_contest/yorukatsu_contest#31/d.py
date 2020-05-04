n, m = map(int, input().split())
prefectures = [[] for _ in range(10 ** 5)]

for i in range(m):
    p, y = map(int, input().split())
    prefectures[p - 1].append([y, i])

ans = [''] * m
for p in range(10 ** 5):
    prefecture = prefectures[p]
    prefecture.sort(key=lambda x: x[0])
    for i in range(len(prefecture)):
        ans[prefecture[i][1]] = '{:006}{:006}'.format(p + 1, i + 1)

for i in range(m):
    print(ans[i])
