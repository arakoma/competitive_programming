X, Y = map(int, input().split())
ans = 0
if X <= 3:
    ans += (4 - X) * 100000
if Y <= 3:
    ans += (4 - Y) * 100000
if X == 1 and Y == 1:
    ans += 400000

print(ans)

###
N = int(input())
A = list(map(int, input().split()))

L1 = [0]
for i in range(N):
    L1.append(L1[i] + A[i])

L2 = [0]
for i in range(N):
    L2.append(L2[i] + A[-i-1])

x = 100000000000
for i in range(N):
    y = abs(L1[i] - L2[-i-1])
    x = min(x, y)

print(x)

###
H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = [[0] * W for _ in range(H)]
cnt = 0


def xxx(y, x, cnt, d1, d2):
    dy = y + d1
    dx = x + d2
    if 0 <= dy < H and 0 <= dx < W:
        if ans[dy][dx] == 0:
            ans[dy][dx] = cnt
        else:
            return
    else:
        return
    xxx(dy, dx, cnt, d1, d2)


for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            cnt += 1
            ans[i][j] = cnt

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            cnt = ans[i][j]
            xxx(i, j, cnt, 0, 1)
            xxx(i, j, cnt, 0, -1)

for i in range(H):
    for j in range(W):
        if ans[i][j] != 0:
            cnt = ans[i][j]
            xxx(i, j, cnt, -1, 0)
            xxx(i, j, cnt, 1, 0)

for i in range(H):
    print(" ".join(map(str, ans[i])))