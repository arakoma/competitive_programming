N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    nearest_diatance = 4*10**8
    ans = 0
    for j in range(M):
        x = abs(ab[i][0] - cd[j][0])
        y = abs(ab[i][1] - cd[j][1])
        if x+y < nearest_diatance:
            nearest_diatance = x+y
            ans = j+1
    else:
        print(ans)

###############
n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
cd=[list(map(int,input().split())) for j in range(m)]
for a,b in ab:
    abcd=[abs(a-c)+abs(b-d) for c,d in cd]
    print(abcd.index(min(abcd))+1)