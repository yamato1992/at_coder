n = int(input())
nums = list(map(int, input().split()))

ans = pow(200, 2) * 100
for y in range(min(nums), max(nums) + 1):
    cost = 0
    for x in nums:
        cost += pow(x - y, 2)
    ans = min(ans, cost)
print(ans)
