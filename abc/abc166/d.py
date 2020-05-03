x = int(input())
nums = []
i = 0
while i ** 5 <= 10 ** 14:
    nums.append(i ** 5)
    i += 1

for i in range(len(nums)):
    a5 = nums[i]
    for j in range(len(nums)):
        b5 = nums[j]
        if x == a5 - b5:
            print(i, j)
            exit()
        if x == a5 + b5:
            print(i, -j)
            exit()
