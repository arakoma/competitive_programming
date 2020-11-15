N, W = map(int, input().split())
stp = [list(map(int, input().split())) for _ in range(N)]

L = [0 for _ in range(2 * 10**5+5)]

for s, t, p in stp:
    L[s] += p
    L[t] -= p

LL = [0 for _ in range(2 * 10**5+10)]
for i in range(1, len(L)):
    LL[i] += LL[i-1] + L[i-1]

ans = "Yes"
for l in LL:
    if l > W:
        ans = "No"
        break

print(ans)