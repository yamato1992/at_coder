m = int(input())
stars = [list(map(int, input().split())) for _ in range(m)]
n = int(input())
photo = []
for _ in range(n):
    x, y = map(int, input().split())
    photo.append((x, y))

stars.sort()
photo.sort()
slide = []
base_x = stars[0][0]
base_y = stars[0][1]

for x, y in stars:
    slide.append([x - base_x, y - base_y])
slide = slide[1:]

photo_set = set(photo)

ans = [0, 0]
for x, y in photo:
    cnt = 1
    for dx, dy in slide:
        if (x + dx, y + dy) in  photo_set:
            cnt += 1
            continue
        break
    if cnt == m:
        ans = [x - base_x, y - base_y]

print(*ans)
