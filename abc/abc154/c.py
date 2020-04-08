N = int(input())
nums = list(map(int, input().split()))
s = set()
for num in nums:
    if num in s:
        print('NO')
        exit()
    s.add(num)
print('YES')