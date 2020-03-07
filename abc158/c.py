A, B = map(int, input().split())
for n in range(1, 1001):
    a = int(n * 0.08)
    b = int(n * 0.1)
    if A == a and B == b:
        print(n)
        exit()
print(-1)