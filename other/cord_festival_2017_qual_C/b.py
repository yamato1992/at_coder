n = int(input())
A = list(map(int, input().split()))
e = 0
for a in A:
    if a % 2 == 0:
        e += 1
ans = 3 ** n - 2 ** e
print(ans)