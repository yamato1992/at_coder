N = int(input())
names = [0] * 5
pattern = []

def make_pattern(arr, cnt):
    if len(arr) == 5:
        if cnt == 3 :
            pattern.append(arr)
        return
    make_pattern(arr + '1', cnt + 1)
    make_pattern(arr + '0', cnt)

for _ in range(N):
    name = input()
    initial = name[0]
    if 'M' == initial:
        names[0] += 1
    elif 'A' == initial:
        names[1] += 1
    elif 'R' == initial:
        names[2] += 1
    elif 'C' == initial:
        names[3] += 1
    elif 'H' == initial:
        names[4] += 1
    else:
        continue

make_pattern('', 0)

ans = 0
for p in pattern:
    ret = 1
    for i in range(5):
        if p[i] == '1':
            ret *= names[i]
    ans += ret
print(ans) 
