N, K = map(int, input().split())
A = list(map(int, input().split()))

L = [0] * (N+1)
now = 1
p = []
f = False

for i in range(K):
    if L[now] == 1:
        f = True
        break
    p.append(now)
    L[now] = 1
    now = A[now-1]

if f:
    for i in range(len(p)):
        if p[i] == now:
            ans = p[i + (K - i) % len(p[i:])]
            break
else:
    ans = now

print(ans)