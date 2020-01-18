N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]

length = []
for i in range(N):
    s = XL[i][0] - XL[i][1]
    f = XL[i][0] + XL[i][1]
    length.append([s, f])

length = sorted(length, key=lambda x:x[1])
ans = 0
f = - (10**9+7)
for i in range(N):
    if f <= length[i][0]:
        ans += 1
        f = length[i][1] - 0.5

print(ans)