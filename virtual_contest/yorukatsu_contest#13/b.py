n = int(input())
ans = 0
score = []
for _ in range(n):
    score.append(int(input()))

score.sort()
total = sum(score)
if total % 10 == 0:
    for s in score:
        if s % 10 != 0:
            total -= s
            break

print(total if total % 10 != 0 else 0)
