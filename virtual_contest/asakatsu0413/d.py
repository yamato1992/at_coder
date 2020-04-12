n, k = map(int, input().split())
x = list(map(int, input().split()))
time = 3 * 10 ** 8

for i in range(n - k + 1):
    l = x[i]
    r = x[i + k - 1]
    if l * r >= 0:
        total = max(abs(l), abs(r))
    else:
        total = (r - l + min(abs(l), abs(r)))
    time = min(time, total)

print(time)
