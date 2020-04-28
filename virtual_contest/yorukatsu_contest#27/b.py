a, b, c, d = list(input())
for op1 in ['+', '-']:
    for op2 in ['+', '-']:
        for op3 in ['+', '-']:
            tmp = a + op1 + b + op2 + c + op3 + d
            if eval(tmp) == 7:
                print(tmp+'=7')
                exit()
