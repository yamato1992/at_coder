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

    def same(self, x: int, y: int) -> bool:
        return self.find_root(x) == self.find_root(y)

    def size(self, x: int) -> int:
        return (-1) * self.d[self.find_root(x)]