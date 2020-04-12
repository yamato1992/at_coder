def generate(x):
    for i in [3, 5, 7]:
        yield x * 10 + i

n = int(input())
nums = [3, 5, 7]
ans = 0
num = 0
p = 0
while num < n:
    for res in generate(nums[p]):
        nums.append(res)
        num = res
        if res <= n and set(list(str(res))) == set(list(str(357))):
            ans += 1
    p += 1

print(ans)