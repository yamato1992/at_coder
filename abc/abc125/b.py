n = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = 0
for i in range(0, n):
    benefit = values[i] - costs[i]
    if benefit > 0:
        ans += benefit
print(ans)