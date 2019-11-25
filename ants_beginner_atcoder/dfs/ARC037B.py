N, M = map(int, input().split())

#隣接リストで辺の両端を管理
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

#すでに通った頂点
visited = [0] * N


def dfs(now, prev):
    global flag#関数内で関数外の変数を書き換えるのでglobal宣言する
    #辺の張られ先を全て探索
    for next in edge[now]:
        if next != prev:#直前の頂点は除く
            if visited[next] == 1:#閉路
                flag = False
            else:
                visited[next] = 1
                dfs(next, now)


cnt = 0
for i in range(N):
    if not visited[i]:
        flag = True
        dfs(i, -1)#初めはprevに範囲外の値入れる
        if flag:
            cnt += 1

print(cnt)