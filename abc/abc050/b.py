n = int(input())
times = list(map(int, input().split()))
m = int(input())
ans = sum(times)
for i in range(m):
    p, x = map(int, input().split())
    print(ans - times[p - 1] + x)