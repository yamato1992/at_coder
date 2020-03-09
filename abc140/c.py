N = int(input())
b = list(map(int, input().split()))
a = [0] * N
a[0] = b[0]
a[-1] = b[-1]
for i in range(1, N - 1):
    a[i] = min(b[i - 1], b[i])
    print(a)
print(sum(a))
