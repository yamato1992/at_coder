from string import ascii_lowercase

s = list(input())
ans = 'AC'

if s[0] != 'A':
    ans = 'WA'

if s[2:-1].count('C') != 1:
    ans = 'WA'

if not s[1] in ascii_lowercase:
    ans = 'WA'

if not s[-1] in ascii_lowercase:
    ans = 'WA'

for c in s[2:-1]:
    if c == 'C':
        continue
    if not c in ascii_lowercase:
        ans = 'WA'
        
print(ans)