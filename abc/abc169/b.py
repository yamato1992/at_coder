n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
if nums[-1] == 0:
    print(0)
else:
    ans = 1
    for num in nums:
        ans *= num
        if ans > 10 ** 18:
            ans = -1
            break
    print(ans)