import fractions
from functools import reduce


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)


N = int(input())
seq = list(map(int, input().split()))
lcm_num = lcm(seq)

ans = 0
for num in seq:
    ans += (lcm_num - 1) % num

print(ans)
