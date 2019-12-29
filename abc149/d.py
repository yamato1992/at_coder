N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

pattern = []
score = 0

for t in T:
    if t == 'r':
        pattern.append('p')
    elif t == 's':
        pattern.append('r')
    else:
        pattern.append('s')

double = []
single = []
for i in range(K, N - K):
    if pattern[i] == pattern[i - K] and pattern[i] == pattern[i + K]:
        pattern[i] = ''

for i in range(K, N):
    if pattern[i] == pattern[i - K]:
        pattern[i] = ''

for p in pattern:
    if p == 'r':
        score += R
    elif p == 's':
        score += S
    elif p == 'p':
        score += P

print(score)