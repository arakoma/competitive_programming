N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

# dpテーブル
dp = [[0 for _ in range(W+10)] for _ in range(N+5)]

# 初期条件
dp[0][0] = 0

for w in range(W+1):
    for n in range(N):
        Wi = wv[n][0]
        Vi = wv[n][1]
        # 選ぶ場合
        if Wi <= w:
            dp[n+1][w] = max(dp[n][w], dp[n][w-Wi] + Vi)
        # 選ばない場合
        dp[n+1][w] = max(dp[n][w], dp[n+1][w])

print(dp[N][W])