n, m = map(int, input().split())

ss = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(m)]

INF = 10 ** 8 * 4
for s in ss:
    dist = INF
    c_point = 0
    a, b = s
    for i, v in enumerate(p):
        c, d = v
        manhattan = abs(a - c) + abs(b - d)
        if manhattan < dist:
            c_point = i + 1
            dist = manhattan
    print(c_point)
