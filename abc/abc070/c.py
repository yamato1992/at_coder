import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(nums):
    return reduce(lcm_base, nums, 1)

N = int(input())
times = [int(input()) for _ in range(N)]
print(lcm(times))
