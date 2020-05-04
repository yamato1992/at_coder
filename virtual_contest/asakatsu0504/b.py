n = int(input())
words = [input() for _ in range(n)]

ans = 'DRAW'
word_set = set()
tale = words[0][0]

for i in range(n):
    word = words[i]
    head = word[0]
    if tale != head or word in word_set:
        ans = 'WIN' if i % 2 == 1 else 'LOSE'
        break
    tale = word[-1]
    word_set.add(word)

print(ans)