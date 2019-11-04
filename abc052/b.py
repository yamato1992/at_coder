x = 0
ans = 0
n = int(input())
s = list(input())

for c in s:
    if c == 'I':
        x += 1
    else:
        x -= 1
    ans = max(x, ans)

print(ans)
