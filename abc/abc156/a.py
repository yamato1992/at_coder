N, R = map(int, input().split())
if N >= 10:
    print(R)
else:
    print(N - (100 * (10 - N)))
    