N, M , X = map(int, input().split())
book = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9

for i in range(2 ** N):
    money = 0
    L = [0] * M
    for j in range(N):
        if (i >> j) & 1:
            money += book[j][0]
            for m in range(M):
                L[m] += book[j][m+1]
    
    for m in range(M):
        if L[m] < X:
            break
    else:
        ans = min(ans, money)

if ans == 10**9:
    ans = -1

print(ans)
