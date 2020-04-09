o = list(input())
e = list(input())

ans = ''

for x, y in zip(o, e):
    ans += x + y

if len(o) - len(e) == 1:
    ans += o[-1]

print(ans)