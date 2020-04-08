N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    index = 0
    lowest = pow(10, 8) * 4
    for j in range(M):
        dist = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if lowest > dist:
            lowest = dist
            index = j
    print(index + 1)
