from collections import defaultdict

s = input()
move = defaultdict(int)
ans = 'Yes'

for c in s:
    move[c] += 1

if move['N'] > 0 and move['S'] == 0:
    ans = 'No'
if move['S'] > 0 and move['N'] == 0:
    ans = 'No'
if move['W'] > 0 and move['E'] == 0:
    ans = 'No'
if move['E'] > 0 and move['W'] == 0:
    ans = 'No'

print(ans)