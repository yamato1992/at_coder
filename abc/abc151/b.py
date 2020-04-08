N, K, M = map(int, input().split())
scores = list(map(int, input().split()))
req_score = N * M - sum(scores)
if req_score > K:
    print(-1)
elif req_score < 0:
    print(0)
else:
    print(req_score)
