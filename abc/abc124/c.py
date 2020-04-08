S = list(input())
pattern_1 = []
pattern_2 = []
cnt_1 = 0
cnt_2 = 0

for i in range(len(S)):
    if i % 2 == 0:
        pattern_1.append('1')
        pattern_2.append('0')
    else:
        pattern_1.append('0')
        pattern_2.append('1')

for (s, a, b) in zip(S, pattern_1, pattern_2):
    if s != a:
        cnt_1 += 1
    if s != b:
        cnt_2 += 1

print(min(cnt_1, cnt_2))
    