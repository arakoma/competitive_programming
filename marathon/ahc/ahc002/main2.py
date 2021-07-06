import time
from collections import deque


si, sj = map(int, input().split())
T = [list(input().split()) for _ in range(50)]
P = [list(map(int, input().split())) for _ in range(50)]
d = [(0, 1, "R"), (1, 0, "D"), (0, -1, "L"), (-1, 0, "U")]
time_limit = 1.8


def dec_path(si, sj, T, P):
    start_time = time.time()
    # 評価値, 座標, output, visited, 
    value = 0
    ij = [si, sj]
    output = ""
    visited = [[0 for _ in range(50)] for _ in range(50)]

    # 初期
    value += P[si][sj]
    visited[si][sj] = 1
    for di, dj, _ in d:
        ni = ij[0] + di
        nj = ij[1] + dj
        if ni < 0 or 49 < ni or nj < 0 or 49 < nj:
            continue
        if T[ni][nj] == T[si][sj]:
            value += P[ni][nj]
            visited[ni][nj] = 1

    while True:
        i = 0
        j = 0
        n_dirc = ""
        v = 0
        for di, dj, dirc in d:
            ni = ij[0] + di
            nj = ij[1] + dj
            if ni < 0 or 49 < ni or nj < 0 or 49 < nj or visited[ni][nj]:
                continue
            v_tmp = P[ni][nj]
            for ddi, ddj, _ in d:
                nni = ni + ddi
                nnj = nj + ddj
                if nni < 0 or 49 < nni or nnj < 0 or 49 < nnj:
                    continue
                else:
                    if T[nni][nnj] == T[ni][nj]:
                        v_tmp += P[nni][nnj]
                        break
            if v < v_tmp:
                i = ni
                j = nj
                n_dirc = dirc
        if n_dirc != "":
            ij = [i, j]
            output += n_dirc
            visited[i][j] = 1
            value += v
            for ddi, ddj, _ in d:
                nni = i + ddi
                nnj = j + ddj
                if nni < 0 or 49 < nni or nnj < 0 or 49 < nnj:
                    continue
                else:
                    if T[nni][nnj] == T[i][j]:
                        visited[nni][nnj] = 1
                        break

        now_time = time.time() - start_time
        if now_time > time_limit:
            break
    
    """
    for i in range(50):
        print(visited)
    """
    return output


def main():
    output = dec_path(si, sj, T, P)
    print(output)


if __name__ == "__main__":
    main()