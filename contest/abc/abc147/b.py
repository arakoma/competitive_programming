S = input()
N = len(S) 
s1 = S[:N//2]
s2 = S[N//2:][::-1]

cnt = 0
for i in range(N//2):
    if s1[i] != s2[i]:
        cnt += 1

print(cnt)