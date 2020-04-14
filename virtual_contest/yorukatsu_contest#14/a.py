a, b, k = map(int, input().split())
nums = []
upper = min(a, b) + 1
for n in range(1, upper):
    if a % n == 0 and b % n == 0:
        nums.append(n)
print(nums[-k])
