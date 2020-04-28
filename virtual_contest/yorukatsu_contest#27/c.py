n = int(input())
s = list(input())
left = [0] * n
right = [0] * n

for i in range(1, n):
    left[i] = left[i - 1]
    if s[i - 1] == 'W':
        left[i] += 1

for i in range(1, n):
    right[n - i - 1] = right[n - i]
    if s[n - i] == 'E':
        right[n - i - 1] += 1

total = [x + y for x, y in zip(left, right)]
ans = min(total)
print(ans)