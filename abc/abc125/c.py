def gcd(x: int, y: int):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(x % y, y)

N = int(input())
A = list(map(int, input().split()))
L = [A[0]]
R = [A[N - 1]]

for i in range(N - 1):
    L.append(gcd(L[i], A[i + 1]))
    R.append(gcd(R[i], A[N - i - 2]))

R.reverse()

ans = 0
for i in range(0, N):
    if i == 0:
        ans = max(ans, R[i + 1])
    elif i == N -1:
        ans = max(ans, L[i - 1])
    else:
        ans = max(ans, gcd(L[i - 1], R[i + 1]))

print(ans)
