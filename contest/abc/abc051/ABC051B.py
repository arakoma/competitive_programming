K, S = map(int, input().split())

cnt = 0
for x in range(K+1):
    for y in range(K+1):
        z = S - (x + y)
        if 0 <= z <= K:
            cnt += 1

print(cnt)

# 全探索の3重ループだとTLE

# x,yを決めると x+y+z=S となるような z が一意に定まる
# そのようなzが 問題文の条件(0<=z<=K)であり得るか を考える