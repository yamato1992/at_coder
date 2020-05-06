n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
center = sorted_nums[n // 2 - 1]
for num in nums:
    if num <= center:
        print(sorted_nums[n // 2])
    else:
        print(center)