c = [list(map(int, input().split())) for _ in range(3)]

max_1st_row = max(c[0])

for a1 in range(max_1st_row + 1):
    b = []

    for col in range(3):
        b.append(c[0][col] - a1)

    a2 = c[1][0] - b[0]

    if c[1][1] != (a2 + b[1]) or c[1][2] != (a2 + b[2]):
        continue

    a3 = c[2][0] - b[0]

    if c[2][1] != (a3 + b[1]) or c[2][2] != (a3 + b[2]):
        continue

    print('Yes')
    exit()

print('No')                
