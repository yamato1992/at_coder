n = int(input())
height = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(1, n):
    if height[i] > height[i - 1]:
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)