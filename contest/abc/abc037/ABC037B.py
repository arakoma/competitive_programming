N, Q = map(int, input().split())
LRT = [list(map(int, input().split())) for _ in range(Q)]

ans = [0] * N
for i in range(Q):
    L = LRT[i][0]
    R = LRT[i][1]
    T = LRT[i][2]
    for j in range(R-L+1):
        ans[L+j-1] = T

for x in ans:
    print(x)

#############################################
N, Q = map(int, input().split())
LRT = [list(map(int, input().split())) for _ in range(Q)]

T=3#確認してみてね
print(id(T))#確認してみてね

ans = [0] * N
for i in range(Q):
    L = LRT[i][0]
    R = LRT[i][1]
    T = LRT[i][2] 
    #LRT[i][2]のアドレスを参照渡ししてる。(代入してる)
    #Tのアドレスは代入によって更新される(iを更新後のLRTでの場所のアドレスになる)ので、
    #前回のfor(jのやつ)でTを代入した場所の値が、iを更新後のTの値に代わることはない
    for j in range(R-L+1):
        ans[L+j-1] = T 
    else:
        print(id(T))   #確認してみてね
        print(id(LRT[i][2]))#確認してみてね

for x in ans:
    print(x)