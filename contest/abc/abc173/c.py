H, W, K = map(int, input().split())
C = [input() for _ in range(H)]

c = [[] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if C[i][j] == ".":
            c[i].append(0)
        elif C[i][j] == "#":
            c[i].append(1)


sw = []
for i in range(H):
    sw.append(sum(c[i]))

sh = []
for i in range(W):
    s = 0
    for j in range(H):
        s += c[j][i]
    sh.append(s)

S = sum(sw)
ans = 0

for i in range(2 ** H):
    Y = []
    ds = 0
    for h in range(H):
        if (i >> h) & 1:
            ds += sw[h]
            Y.append(h)

    for j in range(2 ** W):
        s = S - ds
        X = []
        for w in range(W):
            if (j >> w) & 1:
                s -= sh[w]
                X.append(w)
        
        for y in Y:
            for x in X:
                s += c[y][x]
        
        if s == K:
            ans += 1

print(ans)


