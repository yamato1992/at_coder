n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
ans = 'No'

for i in range(n - m + 1):
    for j in range(n - m + 1):
        sub_a = [a[i + k][j:j+m] for k in range(m)]
        if sub_a == b:
            ans = 'Yes'

print(ans)
