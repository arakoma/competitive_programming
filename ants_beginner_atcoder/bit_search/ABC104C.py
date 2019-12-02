D, G = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(D)]

ans = 10000
for i in range(2**D):
    s = 0
    cnt = 0
    bit = [0] * D
    
    #各問題についてボーナスまで解くか手を付けないかでbit全探索
    for j in range(D):
        if (i >> j) & 1:
            s += 100 * (j + 1) * pc[j][0] + pc[j][1]
            cnt += pc[j][0]
            bit[j] = 1

    #点数足りないなら追加で解く
    flag1 = False
    flag2 = True
    if s < G:
        for k in range(D)[::-1]:
            if bit[k] == 0:
                for x in range(pc[k][0]):
                    s += 100 * (k + 1)
                    cnt += 1
                    if s >= G:
                        flag1 = True
                        break
                else:
                    flag2 = False
                    break
            if flag1:
                break

    if flag2:
        ans = min(ans, cnt)


print(ans)