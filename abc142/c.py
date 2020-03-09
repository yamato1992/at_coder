N = int(input())
a = list(map(int, input().split()))
ans = [-1] * N
for i in range(N):
    ai = a[i]
    ans[ai - 1] = str(i + 1)
print(' '.join(ans))