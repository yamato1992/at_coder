N = int(input())
h = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(1, N):
    if h[i] <= h[i - 1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)

print(ans)
