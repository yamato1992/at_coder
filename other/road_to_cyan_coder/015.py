from itertools import permutations
from math import factorial
n = int(input())
towns = [list(map(int, input().split())) for _ in range(n)]
path_length = 0
for p in permutations(towns):
    for (x1, y1), (x2, y2) in zip(p, p[1:]):
        path_length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 
ans = path_length / factorial(n)
print(ans)