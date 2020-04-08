N = int(input())
an = list(map(int, input().split()))
over_cnt = 0
colors = []
for a in an:
    rate = a // 400
    if rate >= 8:
        over_cnt += 1
    elif rate not in colors:
        colors.append(rate)
 
print(max(len(colors), 1), len(colors) + over_cnt)