n = int(input())
a = list(map(int, input().split()))
ans = 0
side = []
a.sort(reverse=True)
last = a[0]
for i in range(1, n):
    if last == a[i]:
        side.append(a[i])
        last = 0
    else:
        last = a[i]
    
    if len(side) == 2:
        ans = side[0] * side[1]
        break

print(ans)

        