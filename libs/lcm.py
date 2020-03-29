import math

def lcm(a: int, b: int) -> int:
    return (a * b) // math.gcd(a, b)

a = 6
b = 4
print(lcm(a, b))