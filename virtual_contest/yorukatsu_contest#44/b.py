abcd = list(input())
op = ['+', '-']

for op1 in op:
    for op2 in op:
        for op3 in op:
            formula = abcd[0] + op1 + abcd[1] + op2 + abcd[2] + op3 + abcd[3]
            if eval(formula) == 7:
                print(formula + '=7')
                exit()
