from math import ceil

def divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res

n = int(input())
divs = divisors(n)
divs.sort()
lim = ceil(len(divs) / 2)
ans = 11

for i in range(lim):
    a = divs[i]
    b = divs[(-1) * (i + 1)]
    f = max(len(str(a)), len(str(b)))
    ans = min(ans, f)

print(ans)
