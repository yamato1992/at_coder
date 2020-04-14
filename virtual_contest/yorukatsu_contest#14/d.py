lim = 10 ** 5
ans = [0] * (lim + 1)
like = [1] * (lim + 1)
like[0] = 0
like[1] = 0
for i in range(2, lim + 1):
    if like[i]:
        for j in range(i ** 2, lim + 1, i):
            like[j] = 0

for i in range(3, lim + 1, 2):
    if like[i] and like[(i + 1) // 2]:
        ans[i] = 1

for i in range(2, lim + 1):
    ans[i] += ans[i - 1]

q = int(input())
for _ in range(q):
    r, l = map(int, input().split())
    print(ans[l] - ans[r - 1])
