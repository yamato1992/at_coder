n = int(input())
A = list(map(int, input().split()))[::-1]
B = list(map(int, input().split()))[::-1]
ans = 0

for i, b in enumerate(B):
    ans += min(A[i], b)
    remain = max(0, b - A[i])
    ans += min(A[i + 1], remain)
    A[i + 1] = max(0, A[i + 1] - remain)

print(ans)