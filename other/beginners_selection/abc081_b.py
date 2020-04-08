def shift(nums):
    res = 0
    while True:
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                nums[i] /= 2
            else:
                return res
        res += 1

n = int(input())
nums = list(map(int, input().split()))

print(shift(nums))
