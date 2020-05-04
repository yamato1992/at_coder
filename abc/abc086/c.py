n = int(input())
x = 0
y = 0
t = 0
ans = 'Yes'

for _ in range(n):
    ti, xi, yi = map(int, input().split())
    elapsed_time = ti - t
    if abs(x - xi) + abs(y - yi) > elapsed_time:
        ans = 'No'
        break
    dist_odd_even = (abs(x - xi) + abs(y - yi)) % 2
    time_odd_even = elapsed_time % 2
    if dist_odd_even != time_odd_even:
        ans = 'No'
        break
    x = xi
    y = yi
    t = ti

print(ans)