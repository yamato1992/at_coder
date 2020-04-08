S = list(input())
N = len(S)
ans = 'No'
if S == S[::-1]:
    sub_1 = S[:(N - 1) // 2]
    if sub_1 == sub_1[::-1]:
        sub_2 = S[(N + 2) // 2:]
        if sub_2 == sub_2[::-1]:
            ans = 'Yes'
print(ans)