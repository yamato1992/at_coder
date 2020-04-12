a, b = map(int, input().split())
s = list(input())
ans = 'Yes'

if '-' in s[:a]:
    ans = 'No'
if '-' != s[a]:
    ans = 'No'
if '-' in s[a + 1:]:
    ans = 'No'

print(ans)