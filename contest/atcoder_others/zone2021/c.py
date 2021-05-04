N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

ans = 0
p_max = [0 for _ in range(5)]

for m in M:
    for i in range(5):
        p_max[i] = max(p_max[i], m[i])

for i in range(N-1):
    for j in range(i+1, N):
        p = [0 for _ in range(5)]
        pmin = 10**9
        idx = 0
        for k in range(5):
            p[k] = max(M[i][k], M[j][k])
            if p[k] < pmin:
                pmin = p[k]
                idx = k
        p[idx] = p_max[idx]
        ans = max(ans, min(p))

print(ans)
