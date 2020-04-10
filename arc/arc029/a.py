n = int(input())
time = [int(input()) for _ in range(n)]
ans = sum(time)
for i in range(1 << n):
    a = 0
    b = 0
    for j in range(n):
        if i >> j & 1:
            a += time[j]
        else:
            b += time[j]
    ans = min(ans, max(a, b))
print(ans)        
