S = list(input())
for i in range(0, len(S), 2):
    if i + 1 < len(S):
        if 'hi' != S[i] + S[i + 1]:
            print('No')
            exit()
    else:
        print('No')
        exit()
print('Yes')