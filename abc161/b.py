n, m = map(int, input().split())
a = list(map(int, input().split()))
votes = sum(a)
a.sort(reverse=True)
ans = 'Yes'
for i in range(m):
    if a[i] < votes / (4 * m):
        ans = 'No'
        break
print(ans)
