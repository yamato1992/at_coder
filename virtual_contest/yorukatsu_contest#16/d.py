def generate(num):
    n = int(str(num)[-1])
    if n != 0:
        yield num * 10 + n - 1
    yield num * 10 + n
    if n < 9:
        yield num * 10 + n + 1

k = int(input())
lunlun = [i for i  in range(1, 10)]
p = 0
while len(lunlun) < k:
    for l in generate(lunlun[p]):
        lunlun.append(l)
    p += 1
print(lunlun[k - 1])