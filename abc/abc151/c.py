N, M = map(int, input().split())

wa_stock = [0] * N
ac = 0
wa = 0
stat = ['NA'] * N

for _ in range(M):
    p, S = input().split()
    key = int(p) - 1
    if S == 'WA':
        wa_stock[key] += 1
    elif stat[key] != 'AC' and S == 'AC':
        stat[key] = 'AC'
        ac += 1
        wa += wa_stock[key]

print(ac, wa)
