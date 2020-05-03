N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

G = [0] * N

for a, b in AB:
    a -= 1
    b -= 1
    G[a] = max(G[a], H[b])
    G[b] = max(G[b], H[a])

ans = 0
for i in range(N):
    if G[i] < H[i]:
        ans += 1

print(ans)