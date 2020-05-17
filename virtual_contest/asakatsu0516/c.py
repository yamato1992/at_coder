from collections import defaultdict
n = int(input())
bars = list(map(int, input().split()))
bars.sort(reverse=True)
sides = defaultdict(int)
decided = []
ans = 0

for b in bars:
    sides[b] += 1
    if sides[b] == 2:
        decided.append(b)
        sides[b] -= 2
    if len(decided) == 2:
        ans = decided[0] * decided[1]
        break

print(ans)