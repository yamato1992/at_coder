s = input()[::-1]
sum_of_digits = 0
cnts = [0] * 2019
cnts[0] = 1

d = 1
for c in s:
    sum_of_digits += int(c) * d
    d *= 10
    d %= 2019
    sum_of_digits %= 2019
    cnts[sum_of_digits] += 1

ans = 0
for cnt in cnts:
    ans += cnt * (cnt - 1) // 2

print(ans)
