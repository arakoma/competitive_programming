N, M = map(int, input().split())
ps = [tuple(input().split()) for _ in range(M)]

idx = list(range(N+1))
wa = [0] * (N + 1)
AC = 0
WA = 0
for i in range(len(ps)):
    if idx[int(ps[i][0])] != "AC":
        if ps[i][1] == "AC":
            AC += 1
            idx[int(ps[i][0])] = "AC"
        else:
            wa[int(ps[i][0])] += 1

for i in range(N+1):
    if idx[i] == "AC":
        WA += wa[i] 

print(str(AC) + " " + str(WA))