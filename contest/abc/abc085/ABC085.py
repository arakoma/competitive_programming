n = int(input())
d = [int(input()) for _ in range(n)]

print(len(set(d)))
#list要素の重複を消すには
#set()で集合型にする