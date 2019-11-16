N, K = map(int, input().split())
nums = []
for _ in range(N):
    a, b = map(int, input().split())
    nums.append([a, b])
cnt = 0
nums.sort()
for num in nums:
    cnt += num[1]
    if cnt >= K:
        print(num[0])
        break
