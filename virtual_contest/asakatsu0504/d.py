n = int(input())
A = list(map(int, input().split()))

for i in range(2, n):
    A[i] += A[i - 2]

ans = (-50) * 50
for i in range(n):
    a_point = (-50) * 50
    t_point = 0
    for j in range(n):
        if i == j:
            continue

        a = A[max(i, j)]
        b = A[max(i, j) - 1]
        if abs(i - j) % 2 == 1:
            if min(i, j) - 1 >= 0:
                a -= A[min(i, j) - 1]
            if min(i, j) - 2 >= 0:
                b -= A[min(i, j) - 2]
        else:
            if min(i, j) - 1 >= 0:
                b -= A[min(i, j) - 1]
            if min(i, j) - 2 >= 0:
                a -= A[min(i, j) - 2]
        
        if abs(i - j) % 2 == 1:
            aoki = a
            takahashi = b
        else:
            aoki = b
            takahashi = a

        if aoki > a_point:
            a_point = aoki
            t_point = takahashi
    ans = max(ans, t_point)

print(ans)
