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
ans = 10 ** 12
divs.sort()
for i in range(ceil(len(divs) / 2)):
    a = divs[i]
    b = divs[(i + 1) * (-1)]
    ans = min(ans, (a - 1) + (b - 1))

print(ans)