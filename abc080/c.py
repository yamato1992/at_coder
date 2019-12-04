N = int(input())
f = [list(map(int, input().split())) for _ in range(N)]
p = [list(map(int, input().split())) for _ in range(N)]

ans = []
stk = []

stk.append([0] * N)

for i in range(10):
    len_stk = len(stk)
    for j in range(len_stk):
        total = 0
        arr = []
        for k in range(N):
            open_cnt = stk[j][k] + f[k][i]
            arr.append(open_cnt)
            total += p[k][open_cnt]
        ans.append(total)
        stk.append(arr)

print(max(ans))
