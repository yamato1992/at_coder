w, h, n = map(int, input().split())
min_x = 0
min_y = 0
max_x = w
max_y = h

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and min_x < x:
        min_x = x
    elif a == 2 and max_x > x:
        max_x = x
    elif a == 3 and min_y < y:
        min_y = y
    elif a == 4 and max_y > y:
        max_y = y

diff_x = max_x - min_x
diff_y = max_y - min_y

if diff_x < 0:
    diff_x = 0
if diff_y < 0:
    diff_y = 0
    
area = diff_x * diff_y
print(area)
