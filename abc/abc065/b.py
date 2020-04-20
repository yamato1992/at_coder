n = int(input())
A = [int(input()) - 1 for _ in range(n)]
pushed = [False] * n
q = [0]
ans = 0
while q:
    b = q.pop()
    ans += 1
    pushed[b] = True
    if pushed[A[b]]:
        ans = -1
        break
    if A[b] == 1:
        break
    q.append(A[b])
print(ans)