n = int(input())
a = list(map(int, input().split()))
spots = [0] + a + [0]
costs = []

for i in range(1, n + 2):
    costs.append(abs(spots[i] - spots[i - 1]))

total = sum(costs)
for i in range(1, n + 1):
    tmp = total
    tmp -= costs[i - 1]
    tmp -= costs[i]
    tmp += abs(spots[i - 1] - spots[i + 1])
    print(tmp)
