n = int(input())
ans = [0] * 6
for _ in range(n):
    MT, mT = map(float, input().split())
    if MT >= 35:
        ans[0] += 1
    elif MT >= 30:
        ans[1] += 1
    elif MT >= 25:
        ans[2] += 1

    if mT >= 25:
        ans[3] += 1

    if mT < 0:
        if MT >= 0:
            ans[4] += 1
        else:
            ans[5] += 1

print(*ans)

    