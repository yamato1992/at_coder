N = int(input())
num = list(map(int, input().split()))
for a in num:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            print('DENIED')
            exit()
print('APPROVED')