S = list(input())
ans = 'Good'
last = ''

for c in S:
    if c == last:
        ans = 'Bad'
    last = c
    
print(ans)