H, N = map(int, input().split())

ans = H

magics = [list(map(int, input().split())) for _ in range(N)]
magics.sort()

h = H
a = 0
b = 0
cnt = 0

while h > 0:
    e = 0
    for i in range(N):
        ai = magics[i][0]
        bi = magics[i][1]
        ei = min(h, ai) / bi
        if ei > e:
            e = ei
            a = ai
            b = bi
    print(h, a, b)
    h -= a
    cnt += b

print(cnt)
