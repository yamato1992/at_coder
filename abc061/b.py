N, M = map(int, input().split())
a = []
b = []

for _ in range(M):
    ai, bi = input().split()
    a.append(ai)
    b.append(bi)

for i in range(1, N + 1):
    print(a.count(str(i)) + b.count(str(i)))
