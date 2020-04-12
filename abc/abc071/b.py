import string
s = set(list(input()))
ans = 'None'
for c in string.ascii_lowercase:
    if not c in s:
        ans = c
        break

print(ans)
