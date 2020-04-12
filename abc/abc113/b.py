n = int(input())
t, a = map(int, input().split())
temp = 10 ** 6
ans = 0
height = list(map(int, input().split()))
for i, h in enumerate(height):
    diff = abs(a - (t - h * 0.006))
    if temp > diff:
        temp = diff
        ans = i + 1
print(ans)