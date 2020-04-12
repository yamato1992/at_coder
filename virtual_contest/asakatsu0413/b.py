h, w = map(int, input().split())
paint = [list(input()) for _ in range(h)]
ans = 'Yes'
for i in range(h):
    for j in range(w):
        if paint[i][j] == '#':
            if i > 0:
                if paint[i - 1][j] == '#':
                    continue
            if i < h - 1:
                if paint[i + 1][j] == '#':
                    continue
            if j > 0:
                if paint[i][j - 1] == '#':
                    continue
            if j < w - 1:
                if paint[i][j + 1] == '#':
                    continue
            ans = 'No'
            break
print(ans)
