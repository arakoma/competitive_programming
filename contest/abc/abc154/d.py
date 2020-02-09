N, K = map(int, input().split())
p = list(map(int, input().split()))

L = [0] * N
for i in range(N):
    L[i] = (p[i] + 1) * p[i] / (2 * p[i])

L2 = [0] * (N + 1)
for i in range(N):
    L2[i+1] = L2[i] + L[i]

x = 0
for i in range(N - K + 1):
    x = max(x, L2[i+K] - L2[i])

print(x)