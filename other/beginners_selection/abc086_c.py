n = int(input())
pre_t = 0
pre_x = 0
pre_y = 0
for i in range(n):
    t, x, y = map(int, input().split())
    distance = abs((x - pre_x) + (y - pre_y))
    past_time = t - pre_t
    if past_time < distance or (distance - past_time) % 2 == 1:
        print('No')
        exit()
    pre_t = t
    pre_x = x
    pre_y = y
print('Yes')
