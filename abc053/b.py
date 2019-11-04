s = list(input())

for i in range(len(s) - 1):
    if s[i] == 'A':
        top = i
        break

for j in range(len(s) - 1, 0, -1):
    if s[j] == 'Z':
        end = j
        break

print(j - i + 1)