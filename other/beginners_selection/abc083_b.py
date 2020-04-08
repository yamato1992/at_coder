n, a, b = map(int, input().split())
res = 0

for i in range(1, n + 1):
    s = str(i)
    sum = 0
    for c in s:
        sum += int(c)
    if sum >= a and sum <= b:
        res += i

print(res)