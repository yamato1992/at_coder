n, m = map(int, input().split())
ac = set()
wa = 0
wa_stock = [0] * n
for _ in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == 'AC' and not p in ac:
        ac.add(p)
        wa += wa_stock[p]
    elif not p in ac:
        wa_stock[p] += 1
print(len(ac), wa)