from string import ascii_letters

def solve(word):
    for c in ascii_letters:
        sub = word + c
        if sub in s:
            words.append(sub)
            if len(words) == k:
                print(sub)
                exit()
            solve(sub)

s = input()
k = int(input())
words = []
solve('')