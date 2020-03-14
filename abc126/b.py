S = list(input())
is_yymm = False
is_mmyy = False
yymm_month = int(''.join(S[2:]))
mmyy_month = int(''.join(S[:2]))

if 1 <= yymm_month and yymm_month <= 12:
    is_yymm = True
if 1 <= mmyy_month and mmyy_month <= 12:
    is_mmyy = True

ans = 'NA'
if is_yymm and is_mmyy:
    ans = 'AMBIGUOUS'
elif is_yymm:
    ans = 'YYMM'
elif is_mmyy:
    ans = 'MMYY'

print(ans)