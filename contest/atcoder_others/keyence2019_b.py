S = input()
N = len(S)

ans = "NO"
for i in range(N):
    for j in range(i, N):
        s = S[:i] + S[j:]
        
        if s == "keyence":
            ans = "YES"
            break

print(ans)