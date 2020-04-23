n = int(input())
A = list(map(int, input().split()))
b = [-1] * n
ans = []

for i in range(n - 1, -1, -1):
    cnt = 0
    for j in range(i, n, i + 1):
        if i == j:
            continue
        else:
            if b[j] == 1:
                cnt += 1
    if (A[i] + cnt) % 2 == 0:
        b[i] = 0
    else:
        b[i] = 1
        ans.append(i + 1)

m = len(ans)
print(m)
if m > 0:
    print(*ans)
