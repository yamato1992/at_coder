n, m = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(n)]
checkpoints = [list(map(int, input().split())) for _ in range(m)]
for a, b in students:
    dist = 4 * 10 ** 8
    ans = 0
    for j in range(m):
        c, d = checkpoints[j]
        tmp = abs(a - c) + abs(b - d)
        if dist > tmp:
            dist = tmp
            ans = j + 1
    print(ans)
