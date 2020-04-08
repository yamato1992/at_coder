n = int(input())

def generate(p):
    for i in [3, 5, 7]:
        yield p * 10 + i

nums = [3, 5, 7]
ans = 0
num = 0
p = 0

while num < n:
    for a in generate(nums[p]):
        nums.append(a)
        num = a
        if a <= n and set(list(str(a))) == set(list(str(357))):
            ans += 1
    p += 1

print(ans)