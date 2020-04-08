N, K = map(int, input().split())
nums = list(map(int, input().split()))

pos = []
neg = []
zero = []

for n in nums:
    if n < 0:
        neg.append(n)
    elif n > 0:
        pos.append(n)
    else:
        zero.append(n)

neg.sort()
pos.sort()
len_neg = len(neg)
len_pos = len(pos)
len_zero = len(zero)
neg_pattern = len_neg * len_pos
pos_pattern = (len_pos * (len_pos - 1) // 2) * (len_neg * (len_neg - 1) // 2)
zero_pattern = (len_neg + len_pos) * len_zero

if K <= neg_pattern:
    res = []
    for minus in neg:
        for plus in pos:
            res.append(minus * plus)
    res.sort()
    print(res[K - 1])
elif K <= (neg_pattern + zero_pattern):
    print(0)
else:
    res = []
    for i in range(len_neg - 1):
        for j in range(i + 1, len_neg):
            res.append(neg[i] * neg[j])
    
    for i in range(len_pos - 1):
        for j in range(i + 1, len_pos):
            res.append(pos[i] * pos[j])
    res.sort()
    pattern = (N * (N - 1)) // 2
    index = -1 * (pattern - K + 1)
    print(res[index])
