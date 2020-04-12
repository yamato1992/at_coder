n = int(input())
a = list(map(int, input().split()))
p = a[0]
ans = 1
stat = 'None'
for i, ai in enumerate(a, 1):
    if stat == 'None':
        if ai < p:
            stat = 'Down'
        elif ai > p:
            stat = 'Up'
    else:
        if ai < p and stat == 'Up':
            ans += 1
            stat = 'None'
        elif ai > p and stat == 'Down':
            ans += 1
            stat = 'None'
    p = ai
print(ans)
