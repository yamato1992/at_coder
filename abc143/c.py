N = int(input())
S = list(input())
s = list(S[0])
for c in S[1:]:
    if not c == s[-1]:
        s.append(c)
print(len(s))