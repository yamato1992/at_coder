import sys
sys.setrecursionlimit(10 ** 9)

class Union_Find:
    def __init__(self, n = 0):
        self.d = [-1] * n

    def find_root(self, x: int) -> int:
        if self.d[x] < 0:
            return x
        self.d[x] = self.find_root(self.d[x])
        return self.d[x]

    def unite(self, x: int, y: int) -> bool:
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def is_same(self, x: int, y: int) -> bool:
        return self.find_root(x) == self.find_root(y)

    def size(self, x: int) -> int:
        return (-1) * self.d[self.find_root(x)]

n, m, k = map(int, input().split())
uf = Union_Find(n)
ng = [set() for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ng[a].add(b)
    ng[b].add(a)
    uf.unite(a, b)

for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.is_same(c, d):
        ng[c].add(d)
        ng[d].add(c)

ans = [0] * n
for i in range(n):
    ans[i] = uf.size(i) - len(ng[i]) - 1

print(*ans)
