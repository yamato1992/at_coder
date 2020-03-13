N = int(input())
h = list(map(int, input().split()))[::-1]
f = [0] * N
ans = 'Yes'
last = 10 ** 10
for hi in h:
    if last >= hi:
        last = hi
    elif last >= hi - 1:
        last = hi - 1
    else:
        ans = 'No'

print(ans)
