import math
 
N = int(input())
cities = []
 
for _ in range(N):
  x, y = map(int, input().split())
  cities.append([x, y])
 
total = 0
for i in range(N):
    for j in range(i + 1, N):
        xi, yi = cities[i]
        xj, yj = cities[j]
        total += math.sqrt(pow(xi - xj, 2) + pow(yi - yj, 2))   
print(total * 2 / N)