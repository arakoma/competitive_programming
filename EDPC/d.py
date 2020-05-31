N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(W+10)] for _ in range(N+5)]

for w in range(1, W+1):
    for n in range(N):
        Wi = wv[n][0]
        Vi = wv[n][1]
        if Wi <= w:
            dp[n+1][w] = max(dp[n][w], dp[n][w-Wi] + Vi)
        dp[n+1][w] = max(dp[n][w], dp[n+1][w])

print(dp[N][W])