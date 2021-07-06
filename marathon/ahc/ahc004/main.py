import random
import time

def input_all():
    N, M = map(int, input().split())
    S = [input() for _ in range(M)]

    return N, M, S


def output_all(output):
    for out in output:
        print(out)


def calc_score(mat, S, M):
    # . の数
    d = 0
    # 転置ver
    mat_t = []
    for i in range(20):
        r = ""
        for j in range(20):
            r += mat[j][i]
            if mat[j][i] == ".":
                d += 1
        mat_t.append(r)
    
    # 部分文字列判定
    c = 0
    for s in S:
        for i in range(20):
            if (s in mat[i]+mat[i]) or (s in mat_t[i]+mat_t[i]):
                c += 1
                break
    
    # 得点計算
    score = 0
    if c < M:
        score = 10**8 * c // M
    elif c == M:
        score = 10**8 * 2 * 20**2 / (2 * 20**2 - d) // 0

    return score


if __name__ == "__main__":
    start_time = time.time()
    A = "ABCDEFGH"

    N, M, S = input_all()
    S = set(S)
    S = list(S)

    # 初期値
    best_ans = ["" for _ in range(20)]
    best_score = 0
    """
    idx = 0
    for i in range(20):
        s = ""
        for j in range(idx, M):
            s += S[i]
            idx += 1
            if len(s) >= 20:
                s = s[:20]
                break
        best_ans[i] = s
    """
    S.sort(key=lambda x: len(x), reverse=True)
    for i in range(20):
        s = S[i]
        for j in range(20-len(s)):
            s += random.choice(A)
        best_ans[i] = s
        
    best_score = calc_score(best_ans, S, M)

    # 焼きなまし
    ans = best_ans.copy()
    while True:
        l = random.randrange(0, 19)
        r = random.randrange(l+1, 20)
        u = random.randrange(0, 19)
        b = random.randrange(u+1, 20)
        for i in range(u, b):
            s = ""
            for _ in range(l, r):
                s += random.choice(A)
            if r == 20:
                ans[i] = ans[i][:l] + s
            elif r < 20:
                ans[i] = ans[i][:l] + s + ans[i][r:]
        score = calc_score(ans, S, M)
        if score > best_score:
            best_ans = ans.copy()
            best_score = score
        if time.time() - start_time > 2.8:
            break
    
    output_all(best_ans)
    #print(best_score)