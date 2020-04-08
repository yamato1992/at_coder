def beautiful_strings(w):
    d = {}
    for c in w:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for val in d.values():
        if val % 2 == 1:
            return 'No'
    return 'Yes'

w = input()
print(beautiful_strings(w))
