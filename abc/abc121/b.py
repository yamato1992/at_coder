N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for _ in range(N):
    A = list(map(int, input().split()))
    score = C
    for (ai, bi) in zip(A, B):
        score += ai * bi
    if score > 0:
        ans += 1
print(ans)