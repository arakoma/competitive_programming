w=list(input())
alpha=list('abcdefghijklmnopqrstuvwxyz')
for i in alpha:
    if w.count(i)%2 != 0:
        print('No')
        break
else:
    print('Yes')