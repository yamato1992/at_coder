import sys
sys.setrecursionlimit(10 ** 9)

class Union_Find:
    def __init__(self, n = 0):
        self.d = [-1] * n
    
    def find(self, x: int) -> int:
        if self.d[x] < 0:
            return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]
    
    def unite(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return -1 * self.d[self.find(x)]


n, m, k = map(int, input().split())
uf = Union_Find(n)

friends = [0] * n
blocks = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friends[a] += 1
    friends[b] += 1
    uf.unite(a, b)

for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    blocks[c].append(d)
    blocks[d].append(c)

ans = []
for i in range(n):
    candidates = uf.size(i) - 1 - friends[i]
    for u in blocks[i]:
        if uf.same(i, u):
            candidates -= 1
    ans.append(candidates)

print(*ans)
