cards = {i: list(input()) for i in 'abc'}
next = 'a'
while cards[next]:
    next = cards[next].pop(0)
print(next.upper())