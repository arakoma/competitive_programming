N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

INF = W + 10
dp = [[INF for _ in range(N*10**3+10)] for _ in range(N+1)]

dp[0][0] = 0
for sum_v in range(N*10**3+1):
    for n in range(N):
        Wi = wv[n][0]
        Vi = wv[n][1]
        if sum_v - Vi >= 0:
            dp[n+1][sum_v] = min(dp[n][sum_v], dp[n][sum_v-Vi] + Wi)
        dp[n+1][sum_v] = min(dp[n][sum_v], dp[n+1][sum_v])

ans = 0
for sum_v in range(len(dp[N])):
    if dp[N][sum_v] <= W:
        ans = sum_v

print(ans)
