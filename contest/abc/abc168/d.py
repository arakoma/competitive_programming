N, M = map(int, input().split())
L = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

ans = [0 for _ in range(N+1)]
now = [1]
next = []

while len(now):
    for x in now:
        for y in L[x]:
            if ans[y] == 0:
                ans[y] = x
                next.append(y)
    now = next.copy()
    next = []

print("Yes")
for x in range(2, N+1):
    print(ans[x])