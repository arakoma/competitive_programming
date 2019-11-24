n = int(input())

for i in range(n//4+1):
    for j in range(n//7+1):
        if i*4 + j*7 == n:
            print("Yes")
            break
        elif i == n//4 and j == n//7:
            print("No")
            break
    else:
        continue
    break

##########################
#2重ループ抜ける方法について

#10以下かつ足して10になるような最小のi,jを出力(i,jの全組み合わせを考える)

#else:continue使う
for i in range(10):
    for j in range(10):
        if i+j == 10:
            print(i)
            print(j)
            break#for(j)を抜ける(elseごと抜ける)
    else:#for(j)が終わるとelseに入る
        continue#次のfor(i)へ戻る(これ以降の文は実行されない)
    break#for(j)から抜けるとこれが実行されてfor(i)から抜ける
#forの後にelse置くと、forが終わった時にelseを実行する
#for~elseまでで1まとまりのfor文と考えてね

#flag立てる
flag = False
for i in range(10):
    for j in range(10):
        if i+j == 10:
            print(i)
            print(j)
            flag = True
            break
    if flag:
        break
#こっちの方が分かりやすいかな？
#(for-elseはpythonの仕様知らないと分らんので)
