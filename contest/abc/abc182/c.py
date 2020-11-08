N = input()

INF = 10**9
ans = INF
for i in range(1, 2**len(N)):
    s = ""
    for j in range(len(N)):
        if (i >> j) & 1:
            s += N[j]
    if int(s) % 3 == 0:
        ans = min(ans, len(N) - len(s))

if ans == INF:
    ans = -1

print(ans)