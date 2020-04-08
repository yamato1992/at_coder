S = list(input())
pattern = 'ACGT'
ans = 0
length = 0

for c in S:
    if c in pattern:
        length += 1
        ans = max(ans, length)
    else:
        length = 0

print(ans)
