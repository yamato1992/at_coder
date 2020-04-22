from collections import defaultdict
n, m = map(int, input().split())
A = list(map(int, input().split()))
cards = defaultdict(int)

for a in A:
    cards[a] += 1

for i in range(m):
    b, c = map(int, input().split())
    cards[c] += b

cards = sorted(cards.items(), key=lambda x: -x[0])

ans = 0
i = 0
while n > 0:
    num, cnt = cards[i]
    ans += num * min(cnt, n)
    n -= cnt
    i += 1
print(ans)