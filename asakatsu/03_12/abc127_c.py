N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

L_max = 0
R_min = N
for L, R in LR:
    L_max = max(L_max, L)
    R_min = min(R_min, R)

ans = 0
if L_max <= R_min:
    ans = R_min - L_max + 1

print(ans)