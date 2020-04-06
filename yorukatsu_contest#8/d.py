h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
memo = [[0 for _ in range(w)] for _ in range(h)]
step = [[1, 0], [-1, 0], [0, 1], [0, -1]]

memo[0][0] = 1
white = 0
for row in maze:
    white += row.count('.')

q = [[0, 0, 0]]

while q:
    x, y, c = q.pop(0)
    for a, b in step:
        next_x = x + a
        next_y = y + b
        if next_x == h - 1 and next_y == w - 1:
            print(white - (c + 2))
            exit()
        if next_x >= h or next_x < 0:
            continue
        if next_y >= w or next_y < 0:
            continue
        if memo[next_x][next_y] == 1:
            continue
        if maze[next_x][next_y] == '#':
            continue
        memo[next_x][next_y] = 1
        q.append([next_x, next_y, c + 1])
print(-1)
