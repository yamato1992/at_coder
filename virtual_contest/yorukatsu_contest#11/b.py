nums = list(map(int, input().split()))

odd = 0
even = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 0

if odd != 3 and even != 3:
    for i in range(3):
        if odd > even and nums[i] % 2 == 1:
            nums[i] += 1
        elif even > odd and nums[i] % 2 == 0:
            nums[i] += 1
    ans += 1

m = max(nums)
for n in nums:
    ans += (m - n) // 2

print(ans)
