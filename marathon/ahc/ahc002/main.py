import time
from collections import deque


si, sj = map(int, input().split())
T = [list(input().split()) for _ in range(50)]
P = [list(map(int, input().split())) for _ in range(50)]
d = [(0, 1, "R"), (1, 0, "D"), (0, -1, "L"), (-1, 0, "U")]
time_limit = 1.9
q_restart = 10


def dec_path(si, sj, T, P):
    start_time = time.time()
    visited = [[0 for _ in range(50)] for _ in range(50)]
    q = deque()
    best = calc_value(0, [si, sj], "", visited)
    # 評価値, 座標, output, visited, 
    q.append(best)
    q_L = []
    cnt = 0

    while q:
        value, ij, out, visited = q.popleft()
        for di, dj, dirc in d:
            i_next = ij[0] + di
            j_next = ij[1] + dj
            x = calc_value(value, (i_next, j_next), out + dirc, visited)
            if x != False:
                q_L.append(x)
                cnt += 1

        now_time = time.time() - start_time
        if now_time > time_limit:
            break
        if not q:
            q_L.sort(key=lambda x: x[0], reverse=True)
            if q_L:
                best = q_L[0]
            elif q:
                best = q[0]
            q = deque(q_L[:10])
            q_L = []
    
    if q_L:
        output = q_L[0][2]
    elif q:
        output = q[0][2]
    else:
        output = best[2]

    return output


def calc_value(value, ij, out, visited):
    i = ij[0]
    j = ij[1]
    if i < 0 or 49 < i or j < 0 or 49 < j or visited[i][j]:
        return False
    value += P[i][j]
    visited[i][j] = 1
    t = T[i][j]
    for di, dj, _ in d:
        ni = i + di
        nj = j + dj
        if ni < 0 or 49 < ni or nj < 0 or 49 < nj:
            continue
        else:
            if T[ni][nj] == t:
                visited[ni][nj] = 1
                break
    
    return [value, ij, out, visited]


def main():
    output = dec_path(si, sj, T, P)
    print(output)


if __name__ == "__main__":
    main()