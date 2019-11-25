N, M = map(int, input().split())

#隣接リストで辺の両端を管理
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

#頂点に訪れたか
visited = [0] * N


def dfs(now, prev):
    global flag
    for next in graph[now]:
        if next != prev:
            if not visited[next]:
                visited[next] = 1
                dfs(next, now)
            else:
                flag = False


cnt = 0
for i in range(N):
    if not visited[i]:
        flag = True
        dfs(i, -1)
        if flag:
            cnt += 1

print(cnt)