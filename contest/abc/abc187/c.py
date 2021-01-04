N = int(input())
S = [input() for _ in range(N)]

S = list(set(S))
SS = []
for s in S:
    SS.append(s[::-1])
SS.sort()

ans = "satisfiable"
for i in range(len(SS)-1):
    if SS[i][0] == "!":
        continue
    if SS[i] == SS[i+1][:-1]:
        ans = SS[i][::-1]
        break

print(ans)