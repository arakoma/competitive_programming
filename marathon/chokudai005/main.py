id, N, K = map(int, input().split())
S = [list(map(int, list(input()))) for _ in range(N)]

"""
1 <= id <= 50
N = 100
K = 9
"""
d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
visited = [[0 for _ in range(N)] for _ in range(N)]


def dfs(y, x, color_num):
    if y < 0 or N <= y or x < 0 or N <= x:
        return
    if visited[y][x]:
        return
    if S[y][x] != color_num:
        return
    
    visited[y][x] = 1
    for dx, dy in d:
        dfs(y+dy, x+dx, color_num)


out = [[] for _ in range(K+1)]
cnt = [0 for _ in range(K+1)]

for c in range(1, K+1):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] or S[i][j] == c:
                continue
            out[c].append([i+1, j+1, c])
            dfs(i, j, S[i][j])
            cnt[c] += 1

cnt_out = 10**6
color = -1
for i in range(1, K+1):
    if cnt[i] < cnt_out:
        cnt_out = cnt[i]
        color = i

# answer
print(cnt_out)
for i in range(cnt_out):
    print(" ".join(map(str, out[color][i])))
