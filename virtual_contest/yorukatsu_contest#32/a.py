from collections import defaultdict
n = int(input())
restaurants = defaultdict(list)
for i in range(n):
    s, p = input().split()
    p = int(p)
    restaurants[s].append([p, i])

cnt = 0
for k, v in sorted(restaurants.items(), key=lambda x: x[0]):
    for p, i in sorted(v, key=lambda x: -x[0]):
        print(i + 1)
