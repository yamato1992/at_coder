def calc(a):
    smallest = a * (a - 1) // 2
    largest = smallest + a * (n - a + 1)
    return largest -smallest + 1

n, k = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0

for a in range(k, n + 2):
    ans += calc(a)
    ans %= mod

print(ans)    
