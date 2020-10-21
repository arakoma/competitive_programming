"""
N, S = input().split()
N = int(N)

ATCG = "ATCG"
r = [[0 for _ in range(N+1)] for _ in range(4)]

for i in range(N):
    for j in range(4):
        if S[i] == ATCG[j]:
            r[j][i+1] += 1
        r[j][i+1] += r[j][i]

Ar = r[0]
Tr = r[1]
Cr = r[2]
Gr = r[3]

ans = 0

for i in range(N):
    for j in range(i+1, N+1):
        a = Ar[j] - Ar[i]
        t = Tr[j] - Tr[i]
        c = Cr[j] - Cr[i]
        g = Gr[j] - Gr[i]
        if a == t and c == g:
            ans += 1

print(ans)
"""
N, S = input().split()
N = int(N)
ans = 0
for i in range(N):
    at = 0
    cg = 0
    for j in range(i, N):
        if S[j] == "A":
            at += 1
        elif S[j] == "T":
            at -= 1
        elif S[j] == "C":
            cg += 1
        elif S[j] == "G":
            cg -= 1
        
        if at == 0 and cg == 0:
            ans += 1

print(ans)