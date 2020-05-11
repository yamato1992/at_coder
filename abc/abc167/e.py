class Combination:
    def __init__(self, n):
        self.fac = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = (self.fac[i - 1] * i) % mod
        self.invmod = [1] * (n + 1)
        self.invmod[n] = pow(self.fac[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.invmod[i - 1] = (self.invmod[i]  * i) % mod
    
    def calc(self, n, k):
        return self.fac[n] * self.invmod[k] % mod * self.invmod[n - k] % mod

n, m, k = map(int, input().split())
mod = 998244353
c = Combination(n)

ans = 0
for i in range(k + 1):
    tmp = c.calc(n - 1, n - i - 1) * m * pow(m - 1, n - i - 1, mod) % mod
    ans = (ans + tmp) % mod

print(ans)
