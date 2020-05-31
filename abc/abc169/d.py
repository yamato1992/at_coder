n = int(input())
d = 2
ans = 0

while d ** 2 <= n:
    if n % d != 0:
        d += 1
        continue
    z = d
    while n % z == 0:
        n //= z
        z *= d
        ans += 1
    
    while n % d == 0:
        n //= d

if n != 1:
    ans += 1

print(ans)