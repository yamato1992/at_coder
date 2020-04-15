n = int(input())
k = int(input())
ans = 0
x = list(map(int, input().split()))
for v in x:
    ans += min(v, k - v) * 2
print(ans)