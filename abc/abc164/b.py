from math import ceil
a, b, c, d = map(int, input().split())
turn_t = ceil(c / b)
turn_a = ceil(a / d)
print('Yes' if turn_t <= turn_a else 'No')