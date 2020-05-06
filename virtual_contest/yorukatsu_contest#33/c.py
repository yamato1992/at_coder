n, k = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
nums.sort(key=lambda x: x[0])
cnt = 0
for a, b in nums:
    cnt += b
    if cnt >= k:
        print(a)
        break