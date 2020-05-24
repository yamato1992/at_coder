n = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    while num % 2 == 0:
        ans += 1
        num //= 2
print(ans)