s = int(input())
nums = [s]
i = 1
for i in range(1, 10 ** 5):
    if nums[i - 1] % 2 == 0:
        n = nums[i - 1] // 2
    else:
        n = nums[i - 1] * 3 + 1 
    if n in nums:
        print(i + 1)
        break
    nums.append(n)

