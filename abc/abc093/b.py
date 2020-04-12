a, b, k = map(int, input().split())

upper = min(a + k, b)
bottom = max(b - k + 1, upper)

for i in range(a, upper):
    print(i)
for j in range(bottom, b + 1):
    print(j)
