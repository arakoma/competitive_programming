s = list(input())
t = list(input())

for i in range(len(s)):
    s.insert(0, s[-1])
    del s[-1]#removeは最初に出る値を検索して削除なのでdelで位置指定して削除する
    if s == t:
        print("Yes")
        break
    elif i == len(s)-1:
        print("No")
