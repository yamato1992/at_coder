N, K, Q = map(int, input().split())
scores = [K - Q] * N
for _ in range(Q):
    ai = int(input()) - 1
    scores[ai] += 1
for s in scores:
    if s > 0:
        print('Yes')
    else:
        print('No')