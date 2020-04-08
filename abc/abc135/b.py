N = int(input())
p = list(map(int, input().split()))
s = sorted(p)
swap = 1
swap_pattern = [n * 2 for n in range(swap + 1)]
cnt = 0
ans = 'YES'

for (pi, si) in zip(p, s):
    if pi != si:
        cnt += 1

if not cnt in swap_pattern:
    ans = 'NO'

print(ans)
