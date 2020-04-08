N = int(input())
S = input()
string = 'ABC'
ans = 0
for i in range(N - 2):
    if S[i:i+len(string)] == string:
        ans += 1
print(ans)