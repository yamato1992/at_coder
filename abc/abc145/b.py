N = int(input())
S = list(input())

print(S[:N/2], S[N/2:])

if S[:N/2] == S[N/2:]:
    print('Yes')
else:
    print('No')
