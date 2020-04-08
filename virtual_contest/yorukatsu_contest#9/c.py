n, m = map(int, input().split())
nums = []
for i in range(1000):
    if len(str(i)) == n:
        nums.append(i)

for _ in range(m):
    s, c = map(int, input().split())
    next_nums = []
    for a in nums:
        if int(str(a)[s - 1]) == c:
            next_nums.append(a)
    nums = next_nums

print(nums[0] if nums else -1)
