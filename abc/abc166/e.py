from collections import defaultdict
n = int(input())
height = list(map(int, input().split()))
add_set = defaultdict(int)
ans = 0
for i in range(n):
    add_set[i + height[i] + 1] += 1
    if i + 1 - height[i] in add_set:
        ans += add_set[i + 1 - height[i]]

print(ans)
