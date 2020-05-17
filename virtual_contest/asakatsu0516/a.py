n, k = map(int, input().split())
p = set([i for i in range(1, n + 1)])
for _ in range(k):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a in p:
            p.remove(a)
print(len(p))