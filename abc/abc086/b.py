from math import sqrt
a, b = map(int, input().split())
num = int(str(a) + str(b))
if sqrt(num) % 1 == 0:
    print('Yes')
else:
    print('No')