import math

N = int(input())
low = math.ceil(N / 1.08)
up = math.floor(N / 1.08)

if math.floor(low * 1.08) == N:
    print(low)
elif math.floor(up * 1.08) == N:
    print(up)
else:
    print(':(')
