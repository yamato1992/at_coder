from itertools import permutations
n  = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
comb = list(permutations([i for i in range(1, n + 1)]))
comb.sort()
a = 0
b = 0

for i in range(len(comb)):
    if list(comb[i]) == P:
        a = i
    if list(comb[i]) == Q:
        b = i
ans = abs(a - b)
print(ans)