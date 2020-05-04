from collections import defaultdict

n = int(input())
numbers = list(map(int, input().split()))
d = defaultdict(int)

for num in numbers:
    for x in [-1, 0, 1]:
        if num + x >= 0:
            d[num + x] += 1

ans = 0
for k, v in d.items():
    ans = max(ans, v)

print(ans)