N, K = map(int, input().split())
height = list(map(int, input().split()))
ans = 0
for h in height:
    if h >= K:
        ans += 1
print(ans)