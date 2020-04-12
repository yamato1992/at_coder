n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = a[::-1]
b = b[::-1]
ans = 0
for i, bi in enumerate(b):
    ans += min(a[i], b[i])
    remain = max(0, b[i] - a[i])
    ans += min(a[i + 1], remain)
    a[i + 1] = max(0, a[i + 1] - remain)
print(ans)