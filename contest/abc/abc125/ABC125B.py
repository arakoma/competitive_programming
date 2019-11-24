N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

L = []
for i in range(N):
    L.append(V[i] - C[i])

L.sort(reverse=True)
ans = 0
for i in range(N):
    if ans > ans+L[i]:
        break
    else:
        ans += L[i]

print(ans)