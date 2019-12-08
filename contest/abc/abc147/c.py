N = int(input())
xy = []
for i in range(N):
    A = int(input())
    xy.append([])
    for j in range(A):
        xy[i].append(tuple(map(int, input().split())))

ans = 0

for i in range(2 ** N):
    h = [0] * N

    for j in range(N):
        if (i >> j) & 1:
            h[j] = 1
    
    flag = False
    for i in range(N):
        if h[i] == 1:
            for x, y in xy[i]:
                if h[x-1] != y:
                    flag = True
                    break
            if flag:
                break
    
    if not flag:
        ans = max(ans, sum(h))

print(ans)