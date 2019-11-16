from collections import defaultdict

N = int(input())
nums = {}

for _ in range(N):
    a = int(input())
    if a in nums:
        nums[a] = (nums[a] + 1) % 2
    else:
        nums[a] = 0

cnt = 0

for key,value in nums.items():
    if value == 0:
        cnt += 1

print(cnt)
