n = int(input())
kinds = len(set(list(input().split())))
print('Four' if kinds == 4 else 'Three')
