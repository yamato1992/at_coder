from collections import defaultdict
cards = defaultdict(int)
n = int(input())
for _ in range(n):
    s = input()
    cards[s] += 1
m = int(input())
for _ in range(m):
    t = input()
    cards[t] -= 1
ans = 0
for k, v in cards.items():
    ans = max(ans, v)
print(ans)