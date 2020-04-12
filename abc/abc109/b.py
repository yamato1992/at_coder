n = int(input())
ans = 'Yes'
words = [input() for _ in range(n)]
said = set()
tail = words[0][0]
for w in words:
    if w in said or w[0] != tail:
        ans = 'No'
        break
    said.add(w)
    tail = w[-1]

print(ans)