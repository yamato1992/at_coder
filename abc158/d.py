# Not solve
s = list(input())
Q = int(input())
rev = 0
for i in range(Q):
    query = input()
    ti = list(query)[0]
    if ti == '1':
        rev = (rev + 1) % 2
    else:
        ti, fi, ci = query.split()
        if (int(fi) + rev) == 2:
            s.append(ci)
        else:
            s.insert(0, ci)
if rev == 1:
    s.reverse()
print(''.join(s))