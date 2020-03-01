N, M = map(int, input().split())
sc = [tuple(map(int, input().split())) for _ in range(M)]

num = [999] * N

no = 99999999999999
L = []
for s, c in sc:
    if s in L:
        if num[s-1] != c:
            no = -1
    num[s-1] = min(num[s-1], c)
    L.append(s)


if N == 1:
    if num[0] == 999:
        num[0] = 0
else:
    if num[0] == 999:
        num[0] = 1
    elif num[0] < 1:
        no = -1

for i in range(1, N):
    if num[i] == 999:
        num[i] = 0

print(min(int("".join(map(str, num))), no))