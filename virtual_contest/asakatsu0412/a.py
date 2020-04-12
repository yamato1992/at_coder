n, a, b = map(int, input().split())
s = list(input())
pass_all = 0
pass_abroad = 0
for c in s:
    if pass_all < a + b:
        if c == 'a':
            print('Yes')
            pass_all += 1
        elif c == 'b' and pass_abroad < b:
            print('Yes')
            pass_all += 1
            pass_abroad += 1
        else:
            print('No')
    else:
        print('No')