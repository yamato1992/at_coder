n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for xi in x:
    ans += min(xi, k - xi) * 2
print(ans)