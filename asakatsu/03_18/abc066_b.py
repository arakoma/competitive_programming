S = input()

N = len(S)
ans = 0
for i in range(1, N):
    s = S[:N-i]
    n = len(s)
    if n % 2 == 0:
        if s[:n//2] == s[n//2:]:
            ans = n
            break

print(ans)