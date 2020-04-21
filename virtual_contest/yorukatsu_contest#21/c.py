n = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(n - 2):
    a = L[i]
    k = i
    for j in range(i + 1, n - 1):
        b = L[j]
        while k < n and L[k] < a + b:
            k += 1
        ans += k - (j + 1)
print(ans)
