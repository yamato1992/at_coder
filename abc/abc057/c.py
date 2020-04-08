import math
N = int(input())
ans = len(str(N))
for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ans = min(ans, len(str(N // i)))
print(ans)