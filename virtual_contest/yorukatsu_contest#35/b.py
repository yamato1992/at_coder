s = list(input())
k = int(input())
cnt = 0
for c in s:
    if c != '1':
        ans = c
        break
    cnt += 1
    if cnt == k:
        ans = 1
        break
print(ans)