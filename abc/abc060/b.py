A, B, C = map(int, input().split())
ans = 'NO'

for i in range(A, A * B, A):
    if i % B == C:
        ans = 'YES'

print(ans)
