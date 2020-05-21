n = int(input())
maximums = [0, 0]
nums = [int(input()) for _ in range(n)]
maximums = sorted(nums, reverse=True)[:2]
for num in nums:
    if num == maximums[0]:
        print(maximums[1])
    else:
        print(maximums[0])