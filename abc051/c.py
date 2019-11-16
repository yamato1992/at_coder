sx, sy, tx, ty = map(int, input().split())

dist_x = tx - sx
dist_y = ty - sy

print('R' * dist_x, end='')
print('U' * dist_y, end='')

print('L' * dist_x, end='')
print('D' * dist_y, end='')

print('D', end='')
print('R' * (dist_x + 1), end='')
print('U' * (dist_y + 1), end='')
print('L', end='')

print('U', end='')
print('L' * (dist_x + 1), end='')
print('D' * (dist_y + 1), end='')
print('R', end='')
