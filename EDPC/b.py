N, K = map(int, input().split())
H = list(map(int, input().split()))

INF = 10 ** 10
dp = [INF] * N

dp[0] = 0

for i in range(1, N):
    for j in range(min(K, i) + 1):
        dp[i] = min(dp[i], dp[i-j] + abs(H[i] - H[i-j]))

print(dp[N-1])