import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

A, B = map(int, input().split())
print(lcm(A, B))