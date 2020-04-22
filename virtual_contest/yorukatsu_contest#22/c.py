a = list(input())
b = list(input())
c = list(input())
cards = {'a': a, 'b': b, 'c': c}
card = 'a'

while cards[card]:
    card = cards[card].pop(0)

print(card.upper())
