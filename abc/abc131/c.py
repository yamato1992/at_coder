import fractions

def lcm(a, b):
    return (a * b) // fractions.gcd(a, b)

A, B, C, D = map(int, input().split())
n = B - A + 1
n -= (B // C) - ((A - 1) // C)
n -= (B // D) - ((A - 1) // D)
n += (B // lcm(C, D)) - ((A - 1) // lcm(C, D))
print(n)