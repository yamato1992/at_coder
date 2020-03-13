A, B = map(int, input().split())
k = (A + B) / 2
if k % 1 == 0:
    print(int(k))
else:
    print('IMPOSSIBLE')