n = int(input())
d, x = map(int, input().split())
ans = n + x
for _ in range(n):
    a = int(input())
    ans += (d - 1) // a
print(ans)