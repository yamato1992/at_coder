import math
n = int(input())
vehicle = [int(input()) for _ in range(5)]
ans = math.ceil(n / min(vehicle))
print(ans + 4)