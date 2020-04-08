A, B, C, D = list(input())
op = ['+', '-']

for i in range(len(op)):
    for j in range(len(op)):
        for k in range(len(op)):
            op1 = op[i]
            op2 = op[j]
            op3 = op[k]
            state = A + op1 + B + op2 + C + op3 + D
            if eval(state) == 7:
                print(state + '=7')
                exit()
