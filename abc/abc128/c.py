N, M = map(int, input().split())
k = [input().split() for _ in range(M)]
p = list(map(int, input().split()))
ans = 0
for n in range(2 ** N):
    is_mismatch = False
    for i in range(M):
        cnt = 0
        for si in k[i][1:]:
            if (n >> (int(si) - 1)) & 1:
                cnt = (cnt + 1) % 2
        if cnt != p[i]:
            is_mismatch = True
            break
    if not is_mismatch:
        ans += 1
    
print(ans)
    