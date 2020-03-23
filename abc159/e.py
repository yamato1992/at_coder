H, W, K = map(int, input().split())
s = []
INF = (H - 1) + (W - 1)
ans = INF

def add(col: int):
    for i in range(g):
        now[i] += c[i][col]
    for i in range(g):
        if now[i] > K:
            return False
    return True

for _ in range(H):
    s.append(list(input()))

for div in range(1 << (H - 1)):
    g = 0
    id = [0] * H
    for i in range(H):
        id[i] = g
        if div >> i & 1:
            g += 1
    g += 1
    
    now = [0] * g
    num = g - 1
    c = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            c[id[i]][j] += int(s[i][j])

    for j in range(W):
        if not add(j):
            num += 1
            now = [0] * g

            if not add(j):
                num = INF
                break

    ans = min(ans, num)
    
print(ans)