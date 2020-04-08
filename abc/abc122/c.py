N, Q = map(int, input().split())
S = list(input())
cnt = [0] * (N)

for i in range(1, N):
    if S[i - 1] + S[i] == 'AC':
        cnt[i] = cnt[i - 1] + 1
    else:
        cnt[i] = cnt[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    ans = cnt[r - 1] - cnt[l - 1]
    print(ans)
