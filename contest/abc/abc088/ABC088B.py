n = int(input())
a = list(map(int, input().split()))

Alice = []
Bob = []

while 0 < len(a):
    Alice.append(a.pop(a.index(max(a))))
    if 0 < len(a):
        Bob.append(a.pop(a.index(max(a))))

print(sum(Alice) - sum(Bob))
#################################
#大きい順に取るんだからソートしろよ！！！！
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
print(sum(a[0::2])-sum(a[1::2]))