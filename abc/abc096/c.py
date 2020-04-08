H, W = map(int, input().split())
canvas = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if canvas[i][j] == '#':
            up_cell = canvas[i - 1][j] if i > 0 else '.'
            down_cell = canvas[i + 1][j] if i < H - 1 else '.'
            right_cell = canvas[i][j + 1] if j < W - 1 else '.'
            left_cell = canvas[i][j - 1] if j > 0 else '.'
            if up_cell == '.' and down_cell == '.' and right_cell == '.' and left_cell == '.':
                print('No')
                exit()
print('Yes')
