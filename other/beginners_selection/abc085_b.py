n = int(input())
s = {}
for i in range(0, n):
    d = int(input())
    if d in s:
        continue
    else:
        s[d] = 0
print(len(s))