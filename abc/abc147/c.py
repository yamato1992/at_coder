N = int(input())
msg = [[] for _ in range(N)]
for i in range(N):
    ai = int(input())
    for _ in range(ai):
        x, y = map(int, input().split())
        msg[i].append([x - 1, y])

ans = 0
for i in range(1, 2 ** N):
    is_ok = True
    for j in range(N):
        if (i >> j) & 1 == 1:
            for x, y in msg[j]:
                if (i >> x) & 1 != y:
                    is_ok = False
                    break
    if is_ok:
        ans = max(ans, bin(i)[2:].count('1'))
print(ans)