N = int(input())

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

def count_order(group):
    numbers = [i for i in range(1, N + 1)]
    res = 1
    for i in range(len(group) - 1):
        num = group[i]
        res += numbers.index(num) * pattern[-(i + 1)]
        numbers.pop(numbers.index(num))
    return res


P = list(map(int, input().split()))
Q = list(map(int, input().split()))

pattern = [factorial(i) for i in range(1, N)]
res_p = count_order(P)
res_q = count_order(Q)

print(abs(res_p - res_q))
