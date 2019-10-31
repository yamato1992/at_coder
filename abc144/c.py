import math

INF = 1e12
n = int(input())
cnt = INF
m = math.sqrt(n)

for i in range(1, math.ceil(m) + 1):
  if n % i == 0:
    j = n // i
    cnt = min(cnt, i + j - 2)
  else:
    continue

print(cnt)