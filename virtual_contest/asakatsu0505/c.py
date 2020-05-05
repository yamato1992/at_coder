n = int(input())
cards = list('123456')
for i in range(n % 30):
    f = i % 5
    t = (i % 5) + 1
    cards[t], cards[f] = cards[f], cards[t]
print(''.join(cards))