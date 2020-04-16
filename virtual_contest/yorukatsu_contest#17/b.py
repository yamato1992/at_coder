h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            s[i][j] = 0
            left = max(0, j - 1)
            right = min(w - 1, j + 1)
            up = max(0, i - 1)
            down = min(h - 1, i + 1)
            for k in range(up, down + 1):
                for l in range(left, right + 1):
                    if s[k][l] == '#':
                        s[i][j] += 1

for row in s:
    print(''.join(list(map(str, row))))
