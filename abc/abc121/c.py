from collections import defaultdict

N, M = map(int, input().split())
drinks = defaultdict(int)

for _ in range(N):
    A, B = map(int, input().split())
    drinks[A] += B

drinks = sorted(drinks.items(), key = lambda x : x[0])
cnt = 0
price = 0

for k, v in drinks:
    purchases = min(v, M - cnt)
    cnt += purchases
    price += purchases * k

print(price)
