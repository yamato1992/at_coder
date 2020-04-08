n = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
alice = sum(nums[::2])
bob = sum(nums[1::2])

print(alice - bob)