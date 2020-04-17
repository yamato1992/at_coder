s = input()
n = len(s)
s = s[:-1] if n % 2 == 1 else s[:-2]
while len(s) >= 2:
    n = len(s)
    c = n // 2
    if s[:c] == s[c:]:
        print(n)
        break
    s = s[:-2]
