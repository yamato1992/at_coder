sx, sy, tx, ty = map(int, input().split())

ans = ''
diff_x = tx - sx
diff_y = ty - sy
ans += 'R' * diff_x
ans += 'U' * diff_y
ans += 'L' * diff_x
ans += 'D' * diff_y
ans += 'D'
ans += 'R' * (diff_x + 1)
ans += 'U' * (diff_y + 1)
ans += 'L'
ans += 'U'
ans += 'L' * (diff_x + 1)
ans += 'D' * (diff_y + 1)
ans += 'R'

print(ans)