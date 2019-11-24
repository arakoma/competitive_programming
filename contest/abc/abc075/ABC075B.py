H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            cnt = 0
            if i != 0:
                if j != 0:
                    if S[i-1][j-1] == "#":
                        cnt += 1
                if S[i-1][j] == "#":
                    cnt += 1
                if j != W-1:
                    if S[i-1][j+1] == "#":
                        cnt += 1
            if j != 0:
                if S[i][j-1] == "#":
                    cnt += 1
            if j != W-1:
                if S[i][j+1] == "#":
                    cnt += 1
            if i != H-1:
                if j != 0:
                    if S[i+1][j-1] == "#":
                        cnt += 1
                if S[i+1][j] == "#":
                    cnt += 1
                if j != W-1:
                    if S[i+1][j+1] == "#":
                        cnt += 1
            S[i][j] = str(cnt)
    S_str = "".join(S[i])
    print(S_str)
    S_str = ""

########################
#[-1, 0, 1]でfor回すともっと簡潔に書ける

h, w = map(int, input().split())
S = [list(input()) for i in range(h)]
for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            continue
        cnt = 0
        for dx in [-1, 0, 1]:#横
            for dy in [-1, 0, 1]:#縦
                if not 0 <= i+dy <= h-1 or not 0 <= j+dx <= w-1:#端なら無し
                    continue
                if S[i+dy][j+dx] == '#':
                    cnt += 1
        S[i][j] = str(cnt)
for s in S:
    print("".join(s))
