antenna = []
N = 5
for _ in range(N):
    antenna.append(int(input()))
k = int(input())
ans = 'Yay!'
for i in range(N - 1):
    for j in range(1, N):
        if antenna[j] - antenna[i] > k:
            ans = ':('
            break
print(ans)