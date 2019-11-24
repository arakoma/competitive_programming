N, M = map(int, input().split())

L = []
R = []
for i in range(M):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

if min(R)-max(L)+1 <= 0:
    print(0)
else:
    print(min(R)-max(L)+1)