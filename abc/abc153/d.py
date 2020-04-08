H = int(input())

cnt = 1
hit_point = 1
base = 1
while H > hit_point:
    base *= 2
    cnt += base
    hit_point *= 2
    if hit_point * 2 > H:
        break

print(cnt)