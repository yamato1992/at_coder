N = int(input())
a = list()
tmp = [0, 0]

for _ in range(N):
    ai = int(input())
    a.append(ai)
    if ai > tmp[1]:
        tmp[1] = ai
    elif ai > tmp[0]:
        tmp[0] = ai

m = tmp[1]

for ai in a:
    ans = m
    if ai == m:
        ans = tmp[0]
    print(ans)