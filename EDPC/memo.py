INF = 100
L = [INF] * 3
print(L[0], id(L[0]))
print(L[1], id(L[1]))

L[1] = 999
print(L[0], id(L[0]))
print(L[1], id(L[1]))

# 変数の代入時、新しく(違う場所に)変数を作り直してる

for i in range(2, 2):
    print(i)