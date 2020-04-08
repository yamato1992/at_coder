import math

n = int(input())
ans = math.factorial(n) % (pow(10, 9) + 7)
print(ans)