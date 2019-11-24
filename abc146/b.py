N = int(input())
S = list(input())
for c in S:
    print(chr((ord(c) - ord('A') + N) % 26 + ord('A')), end='')
