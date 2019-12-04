X = int(input())

num_105 = X // 105
for i in range(num_105 + 1):
    remain_money_105 = (X - 105 * i)
    num_104 = remain_money_105 // 104
    for j in range(num_104 + 1):
        remain_money_104 = remain_money_105 - 104 * j
        num_103 = remain_money_104 // 103
        for k in range(num_103 + 1):
            remain_money_103 = remain_money_104 - 103 * k
            num_102 = remain_money_103 // 102
            for l in range(num_102 + 1):
                remain_money_102 = remain_money_103 - 102 * l
                num_101 = remain_money_102 // 101
                for m in range(num_101 + 1):
                    remain_money_101 = remain_money_102 - 101 * m
                    if remain_money_101 % 100 == 0:
                        print(1)
                        exit()
print(0)
