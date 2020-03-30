n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
distance = []
for i in range(1, m):
    distance.append(x[i] - x[i - 1])
distance.sort(reverse=True)
print(sum(distance[n - 1:]))