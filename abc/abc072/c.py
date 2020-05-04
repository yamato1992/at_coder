from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
frequency = defaultdict(int)

for n in nums:
    for x in [-1, 0, 1]:
        if 0 <= n + x and n + x <= 10 **5:
            frequency[n + x] += 1

ans = 0
for k, v in frequency.items():
    ans = max(ans, v)

print(ans)
