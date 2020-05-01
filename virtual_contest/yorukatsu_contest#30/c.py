w, h, n = map(int, input().split())

left = 0
right = w
down = 0
up = h

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        left = max(left, x)
    elif a == 2:
        right = min(right, x)
    elif a == 3:
        down = max(down, y)
    elif a == 4:
        up = min(up, y)

if left >= right or down >= up:
    ans = 0
else:
    ans = (right - left) * (up - down)
print(ans)