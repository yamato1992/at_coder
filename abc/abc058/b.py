O = list(input())
E = list(input())

for i in range(len(O)):
    print(O[i], end='')
    if not len(E) == i:
        print(E[i], end='')
