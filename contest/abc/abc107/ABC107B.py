h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

row = [False] * h
col = [False] * w

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            row[i] = True
            col[j] = True

for i in range(h):
    if row[i]:
        for j in range(w):
            if col[j]:
                print(a[i][j], end = "")#改行しない
        print()#改行
