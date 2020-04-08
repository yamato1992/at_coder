N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.reverse()
b.reverse()
ans = 0
capacity = 0
for i in range(N):
    ans += min(b[i] + capacity, a[i])
    capacity = max(b[i] - max(a[i] - capacity, 0), 0)
ans += min(a[-1], capacity)
print(ans)