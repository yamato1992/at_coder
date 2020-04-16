s = input()
t = input()

n = len(s)
p = 0
ans = 'No'
for i in range(n):
    if s[i] == t[0]:
        tmp = s[i:] + s[:i]
        if tmp == t:
            ans = 'Yes'
print(ans)