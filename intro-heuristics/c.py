D = int(input())#D=365
c = [0] + list(map(int, input().split()))#0<=c<=100
s = [0] + [[0] + list(map(int, input().split())) for _ in range(D)]#0<=s<=20000

t = [0] + [int(input()) for _ in range(D)]

M = int(input())
dq = [list(map(int, input().split())) for _ in range(M)]


held = [[0] for _ in range(27)]#選んだ日を保持
def culc_value(t):
    last = [0] * 27
    value = 0
    for d in range(1, D+1):
        type = t[d]
        held[type].append(d)
        value += s[d][type]
        last[type] = d
        for i in range(1, 27):
            value -= c[i] * (d - last[i])
    # 最終日+1 を追加、差分修正で前後見るときの後ろの最大値
    for i in range(1, 27):
        held[i].append(D+1)
    #print(held)
    return value


v_lastday = []
value = culc_value(t)

for d, q in dq:
    # 開催日の差分を修正
    value += - s[d][t[d]] + s[d][q]

    # dの前と後のq選択日のみ考えて、その間だけ修正する
    # 変換前のt[d]のマイナス計算を直す
    ind = held[t[d]].index(d)
    r = held[t[d]][ind+1]
    l = held[t[d]][ind-1]
    x = r - l
    value -= ((x + 1) * x // 2) * c[t[d]]
    y = d - l
    z = r - d
    value += (((y + 1) * y // 2) + (z + 1) * z // 2) * c[t[d]]

    del held[t[d]][ind]
    t[d] = q
    held[q].append(d)
    held[q] = sorted(held[q])
    #print(held[q])

    # 変換後のqのマイナス計算
    ind = held[q].index(d)
    r = held[q][ind+1]
    l = held[q][ind-1]
    x = r - l
    value += ((x + 1) * x // 2) * c[q]
    y = d - l
    z = r - d
    value -= (((y + 1) * y // 2) + (z + 1) * z // 2) * c[q]

    v_lastday.append(value)

for ans in v_lastday:
    print(ans)
