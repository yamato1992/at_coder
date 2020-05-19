N = int(input())
H = list(map(int, input().split()))[::-1]
last = 10 ** 10
ans = 'Yes'
for hi in H:
    if last >= hi:
        last = hi
    elif last >= hi - 1:
        last = hi - 1
    else:
        ans = 'No'
print(ans)
