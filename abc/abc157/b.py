A = [list(map(int, input().split())) for _ in range(3)]

N = int(input())
for _ in range(N):
    is_matched = False
    b = int(input())
    for row in range(3):
        for col in range(3):
            if A[row][col] == b:
                is_matched = True
                A[row][col] = True
                if A[row][0] == True and A[row][1] == True and A[row][2] == True:
                    print('Yes')
                    exit()
                elif A[0][col] == True and A[1][col] == True and A[2][col] == True:
                    print('Yes')
                    exit()
                elif A[0][0] == True and A[1][1] == True and A[2][2] == True:
                    print('Yes')
                    exit()
                elif A[0][2] == True and A[1][1] == True and A[2][0] == True:
                    print('Yes')
                    exit()
                break
        if is_matched:
            break
print('No')