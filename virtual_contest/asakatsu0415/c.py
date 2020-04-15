from fractions import gcd
from functools import reduce

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
diff = []
for i in range(N):
    diff.append(abs(x[i] - X))

while len(diff) > 1:
    a, b = diff.pop(), diff.pop()
    diff.append(gcd(a, b))

print(diff[0])
