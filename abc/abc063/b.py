s = input()
words = set()
ans = 'yes'
for c in s:
    if c in words:
        ans = 'no'
        break
    words.add(c)
print(ans)