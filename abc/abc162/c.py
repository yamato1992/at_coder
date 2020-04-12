from math import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

k = int(input())
ans = 0
rev = 0
for i in range(1, k + 1):
    for j in range(i, k + 1):
        tmp = gcd(i, j)
        for l in range(j, k + 1):
            if i == j and j == l:
                ans += i
            elif i == j or j == l or l == i:
                ans += gcd(tmp, l) * 3
            else:
                ans += gcd(tmp, l) * 6
print(ans)
